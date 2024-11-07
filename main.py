from flask import Flask, request, jsonify
from nlp_model import NLPModel
from search_model import SearchModel
from answer_generator import AnswerGenerator

app = Flask(__name__)

# Замените эти переменные на ваши значения API ключа и URL
OPENROUTER_API_KEY = 'your_api_key'
YOUR_SITE_URL = 'your_site_url'
YOUR_APP_NAME = 'your_app_name'

nlp_model = NLPModel(OPENROUTER_API_KEY, YOUR_SITE_URL, YOUR_APP_NAME)
search_model = SearchModel()
answer_generator = AnswerGenerator(OPENROUTER_API_KEY, YOUR_SITE_URL, YOUR_APP_NAME)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')

    # Анализируем вопрос для извлечения ключевых слов
    keywords_response = nlp_model.analyze_question(question)
    keywords = keywords_response.get('choices')[0].get('message').get('content')  # Извлечение ключевых слов из ответа

    # Выполняем поиск в Elasticsearch
    search_results = search_model.search('knowledge_base', keywords)

    # Генерируем ответ на основе результатов поиска
    answer_response = answer_generator.generate_answer(question, search_results)
    answer = answer_response.get('choices')[0].get('message').get('content')  # Извлечение ответа из ответа модели

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)