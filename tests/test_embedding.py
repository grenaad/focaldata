import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tests.data import json_response
from infra.embedding import EmbeddingService
from unittest import mock
import httpx
from http import HTTPStatus

def create_client():
    my_test_client = httpx.Client(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(
                HTTPStatus.OK, text=str(json_response).replace("\'", "\"")
            )
        )
    )
    return my_test_client

def test_embedding():
    service = EmbeddingService("")
    service.embed_model._http_client = create_client()
    result, error = service.embed("some text")
    assert result  == None

