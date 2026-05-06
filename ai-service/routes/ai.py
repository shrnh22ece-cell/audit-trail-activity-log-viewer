from flask import Blueprint, jsonify, g
from services.groq_client import query_ai

bp = Blueprint('ai', __name__, url_prefix='/api/ai')

@bp.route('/prompt', methods=['POST'])
def prompt():
    prompt_text = getattr(g, 'prompt_text', 'Hello from AI service')
    response = query_ai(prompt_text)
    return jsonify({
        'prompt': prompt_text,
        'response': response
    })
