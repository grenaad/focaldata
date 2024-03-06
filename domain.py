from abc import ABC, abstractmethod
from errors import Error

from typing import List
Embedding = List[float]

class IEmbeddingService(ABC):
    @abstractmethod
    def embed(self, text: str) -> tuple[Embedding | None, Error | None]:
        pass

    @abstractmethod
    def similarity(self, embedding1: Embedding, embedding2: Embedding) -> float:
        pass
