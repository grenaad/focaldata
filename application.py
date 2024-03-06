from infra import IEmbeddingService


class Application:
    embeddings_service: IEmbeddingService

    def __init__(self, embeddings_service: IEmbeddingService) -> None:
        self.embeddings_service = embeddings_service

    def search(self, min_age: int, max_age: int):
        print(f"search min age: {min_age}, max age: {max_age}")
        embedding, error = self.embeddings_service.embed("fdfdf")
        if error != None:
            print(str(error))
        else:
            print(embedding)
