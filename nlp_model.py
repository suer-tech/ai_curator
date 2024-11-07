import requests
import json


class NLPModel:
    def __init__(self, api_key, site_url, app_name):
        self.api_key = api_key
        self.site_url = site_url
        self.app_name = app_name

    def analyze_question(self, question):
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
                                "text": f"Извлеки ключевые слова из следующего вопроса: '{question}'"
                            }
                        ]
                    }
                ]
            })
        )

        return response.json()  # Возвращаем ответ от модели

# Пример использования:
# nlp_model = NLPModel(OPENROUTER_API_KEY, YOUR_SITE_URL, YOUR_APP_NAME)
# keywords = nlp_model.analyze_question("Как вернуть аккаунт в Твиттере?")