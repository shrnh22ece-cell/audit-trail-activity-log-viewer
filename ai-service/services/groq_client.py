import logging
import os
import time
from typing import Any, Dict

import requests

logger = logging.getLogger('GroqClient')
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s [GroqClient] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class GroqClient:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        max_retries: int = 3,
        backoff_factor: float = 1.0,
        timeout: int = 20,
    ):
        self.api_key = api_key or os.environ.get('GROQ_API_KEY', '')
        self.base_url = base_url or os.environ.get('GROQ_API_URL', 'https://api.groq.com/openai/v1')
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.timeout = timeout

        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

    def _parse_response(self, response: requests.Response) -> str:
        data = response.json()
        logger.debug('Groq response JSON: %s', data)

        try:
            return data['output'][0]['content'][0]['text'].strip()
        except (KeyError, IndexError, TypeError) as exc:
            raise ValueError(f'Groq response parse error: {exc}') from exc

    def query(self, prompt: str) -> str:
        if not self.api_key:
            message = 'Groq API key not configured.'
            logger.error(message)
            return message

        system_prompt = "You are a helpful AI assistant. Provide accurate, concise, and relevant responses to user queries."
        full_prompt = f"{system_prompt}\n\nUser: {prompt}\n\nAssistant:"

        payload: Dict[str, Any] = {
            'model': 'openai/gpt-oss-20b',
            'input': full_prompt,
            'temperature': 0.7,
            'max_output_tokens': 200,
        }

        last_exception: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            try:
                logger.info('Groq request attempt %d for prompt length %d', attempt, len(prompt))
                response = requests.post(
                    f'{self.base_url}/responses',
                    headers=self.headers,
                    json=payload,
                    timeout=self.timeout,
                )
                response.raise_for_status()
                return self._parse_response(response)
            except requests.RequestException as exc:
                last_exception = exc
                logger.warning('Groq API request failed on attempt %d: %s', attempt, exc)
            except ValueError as exc:
                last_exception = exc
                logger.error('Groq response parse failure on attempt %d: %s', attempt, exc)
                break

            if attempt < self.max_retries:
                backoff = self.backoff_factor * (2 ** (attempt - 1))
                logger.info('Retrying after %.1f seconds...', backoff)
                time.sleep(backoff)

        error_message = 'Groq request failed after multiple retries.'
        logger.error('%s Last error: %s', error_message, last_exception)
        return error_message


_default_client = GroqClient()


def query_ai(prompt: str) -> str:
    return _default_client.query(prompt)
