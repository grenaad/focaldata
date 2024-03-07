import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tests.data import json_response
from infra.store import VectorStore

store = VectorStore()

def test_store():
  min_age = 7
  max_age = 7
  embedding = json_response["data"][0]["embedding"]
  result = store.query(embedding, min_age, max_age, 10)
  assert len(result) == 10
  assert result[0].respondent_id == 53085
  assert result[9].respondent_id == 88678
