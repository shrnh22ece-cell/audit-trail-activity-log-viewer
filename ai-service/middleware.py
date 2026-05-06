import re
from typing import Optional

from flask import g, jsonify, request

PROMPT_INJECTION_PATTERNS = [
    r'ignore (all )?previous instructions',
    r'disregard (all )?previous instructions',
    r'ignore this (message|instruction|prompt)',
    r'follow only the instructions below',
    r'you are now',
    r'this is not a prompt',
    r'ignore any safety',
    r'ignore safety',
    r'do not follow previous instructions',
    r'apply the following rules',
    r'override (all )?prior instructions',
]


def strip_html_tags(text: str) -> str:
    return re.sub(r'<[^>]+>', '', text).strip()


def contains_prompt_injection(text: str) -> bool:
    text_lower = text.lower()
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False


def sanitize_prompt() -> Optional[tuple]:
    if request.path != '/api/ai/prompt' or request.method != 'POST':
        return None

    if not request.is_json:
        return jsonify({'error': 'Request body must be JSON'}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'error': 'Invalid JSON body'}), 400

    prompt_value = data.get('prompt', '')
    if not isinstance(prompt_value, str):
        return jsonify({'error': 'Prompt must be a string'}), 400

    cleaned_prompt = strip_html_tags(prompt_value)
    if contains_prompt_injection(cleaned_prompt):
        return jsonify({'error': 'Prompt rejected due to injection risk'}), 400

    g.prompt_text = cleaned_prompt if cleaned_prompt else 'Hello from AI service'
    return None
