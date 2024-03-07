from domain.contracts import IEmbeddingService, IVectorStore
from domain import MovieResponse
from typing import List


class Application:
    embeddings_service: IEmbeddingService
    store: IVectorStore

    def __init__(self, embeddings_service: IEmbeddingService, store: IVectorStore) -> None:
        self.embeddings_service = embeddings_service
        self.store = store

    def search(self, query: str, min_age: int, max_age: int) -> List[MovieResponse]:
        print(f"Parameters min_age: {min_age}, max_age: {max_age}, query: {query}")
        query_embedding, error = self.embeddings_service.embed(query)
        if query_embedding != None:
          result = self.store.query(query_embedding, min_age, max_age, 10)
          for index, item in enumerate(result):
            print(f"\nRank {index+1}\n{item}")
          return result
        else:
          print(str(error))
          return []

