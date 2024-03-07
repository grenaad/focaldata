from abc import ABC, abstractmethod
from domain import Embedding, MovieResponse
from domain.errors import Error
from typing import List

class IEmbeddingService(ABC):
    @abstractmethod
    def embed(self, text: str) -> tuple[Embedding | None, Error | None]:
        pass


class IVectorStore(ABC):

    @abstractmethod
    def query(self, query_vector: Embedding, min_age: int, max_age: int, count: int) -> List[MovieResponse]:
        pass
