import requests
import json


class AnswerGenerator:
    def __init__(self, api_key, site_url, app_name):
        self.api_key = api_key
        self.site_url = site_url
        self.app_name = app_name

    def generate_answer(self, question, documents):
        context = " ".join([doc['_source']['content'] for doc in documents])  # Объединяем текст документов

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "HTTP-Referer": self.site_url,
                "X-Title": self.app_name,
            },
            data=json.dumps({
                "model": "anthropic/claude-3.5-sonnet",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"На основе следующего контекста сформируй ответ на вопрос: '{question}'. Контекст: {context}"
                            }
                        ]
                    }
                ]
            })
        )

        return response.json()  # Возвращаем ответ от модели

# Пример использования:
# answer_generator = AnswerGenerator(OPENROUTER_API_KEY, YOUR_SITE_URL, YOUR_APP_NAME)
# answer = answer_generator.generate_answer("Как вернуть аккаунт в Твиттере?", results)