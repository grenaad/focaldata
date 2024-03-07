import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tests.data import json_response
from infra.embedding import EmbeddingService
import httpx
from http import HTTPStatus
from domain.errors import EmbeddingServiceAPIAuthenticationError

def create_client(status: HTTPStatus):
    my_test_client = httpx.Client(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(
                status, text=str(json_response).replace("\'", "\"")
            )
        )
    )
    return my_test_client

def test_embedding():
    service = EmbeddingService("")
    service.embed_model._http_client = create_client(HTTPStatus.OK)
    result, error = service.embed("What is the number 1 box office hit")
    assert result != None
    assert error == None
    assert len(result) == 1536

def test_embedding_failed():
    service = EmbeddingService("")
    service.embed_model.timeout = 1.0
    service.embed_model.max_retries = 0
    service.embed_model._http_client = create_client(HTTPStatus.UNAUTHORIZED)
    result, error = service.embed("What is the number 1 box office hit")
    assert result == None
    assert type(error) == EmbeddingServiceAPIAuthenticationError

