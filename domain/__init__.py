from typing import List

from dataclasses import dataclass

Embedding = List[float]

@dataclass
class MovieResponse():
    respondent_id: int
    respondent_name: str
    country: str
    age: int
    response_text: str
    # vector_embedding: Embedding

