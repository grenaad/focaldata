import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from domain.contracts import IVectorStore, IEmbeddingService
from domain import Embedding, MovieResponse
from domain.errors import Error
from typing import List
from application import Application

from unittest import TestCase

class EmbeddingServiceMock(IEmbeddingService):
    embed_return = None, None
    def __init__(self, embed_return) -> None:
        self.embed_return = embed_return

    def embed(self, text: str) -> tuple[Embedding | None, Error | None]:
        return self.embed_return

class VectorStoreMock(IVectorStore):
    query_return = []
    def __init__(self, query_return) -> None:
        self.query_return = query_return
    def query(self, query_vector: Embedding, min_age: int, max_age: int, count: int) -> List[MovieResponse]:
      return self.query_return

movies = [
MovieResponse(
    respondent_id = 1,
    respondent_name = "name 1",
    country = "some country 1",
    age = 4,
    response_text = "some text 1"),
MovieResponse(
    respondent_id = 2,
    respondent_name = "name 2",
    country = "some country 2",
    age = 5,
    response_text = "some text 2")
    ]

class TestEmbedding(TestCase):
  embedding_service = EmbeddingServiceMock(([1.0,2.0], None))
  vector_store = VectorStoreMock(movies)
  def test_correct(self):
    application = Application(self.embedding_service, self.vector_store)
    query = "some query"
    min_age =  3
    max_age = 4
    result = application.search(query, min_age, max_age)
    self.assertTrue(len(result) == 2)
    self.assertTrue(result[0].respondent_id == 1)
