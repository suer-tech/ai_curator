from elasticsearch import Elasticsearch

class SearchModel:
    def __init__(self, es_host='http://localhost:9200'):
        self.es = Elasticsearch([es_host])

    def search(self, index, keywords):
        query = {
            "query": {
                "match": {
                    "content": keywords  # Предполагаем, что текст хранится в поле 'content'
                }
            }
        }
        response = self.es.search(index=index, body=query)
        return response['hits']['hits']  # Возвращаем только найденные документы

# Пример использования:
# search_model = SearchModel()
# results = search_model.search('knowledge_base', 'Твиттер аккаунт')