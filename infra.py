from llama_index.embeddings.openai import OpenAIEmbedding, OpenAIEmbeddingModelType
from llama_index.core.base.embeddings.base import similarity, SimilarityMode
import openai
from domain import Embedding, IEmbeddingService
import errors
from errors import Error

class EmbeddingService(IEmbeddingService):
    embed_model: OpenAIEmbedding

    def __init__(self, openai_api_key: str):
        self.embed_model = OpenAIEmbedding(
            model=OpenAIEmbeddingModelType.TEXT_EMBED_ADA_002, # default
            embed_batch_size=10,
            api_key=openai_api_key,
            timeout = 2.0,
            max_retries = 1
        )

    def embed(self, text: str) -> tuple[Embedding | None, Error | None]:
        try:
            embeddings: Embedding = self.embed_model.get_text_embedding(text)
            return embeddings, None

        except openai.AuthenticationError:
            return None, errors.EmbeddingServiceAPIAuthenticationError()

        except openai.APIConnectionError:
            return None, errors.EmbeddingServiceAPIConnectionError()

        except openai.PermissionDeniedError:
            return None, errors.EmbeddingServiceAPIPermissionDeniedError()

        except openai.RateLimitError:
            return None, errors.EmbeddingServiceAPIRateLimitError()

        except Exception as e:
            error = errors.EmbeddingServiceAPIUnknown(e)
            return None, error

    def similarity(self, embedding1: Embedding, embedding2: Embedding) -> float:
        # SimilarityMode.DEFAULT = "cosine"
        return similarity(embedding1, embedding2, SimilarityMode.DEFAULT)

