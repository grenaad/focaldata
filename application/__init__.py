from domain.contracts import IEmbeddingService, IVectorStore


class Application:
    embeddings_service: IEmbeddingService
    store: IVectorStore

    def __init__(self, embeddings_service: IEmbeddingService, store: IVectorStore) -> None:
        self.embeddings_service = embeddings_service
        self.store = store

    def search(self, query: str, min_age: int, max_age: int):
        print(f"search min age: {min_age}, max age: {max_age}")
        query_embedding, error = self.embeddings_service.embed(query)
        if query_embedding != None:
          self.store.query(query_embedding, min_age, max_age, 10)
        else:
          print(str(error))

