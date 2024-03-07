import pandas as pd
import ast
from pandas import DataFrame
from domain import MovieResponse
from domain.contracts import IVectorStore
from domain.contracts import Embedding
from typing import List
from infra.similarity import similarity_score

# remove warning about updating df slice
pd.set_option('mode.chained_assignment', None)

class VectorStore(IVectorStore):
    columns = ['respondent_id', 'respondent_name', 'country', 'age', 'response_text','vector_embedding']
    df: DataFrame
    def __init__(self) -> None:
      self.df = pd.read_csv('./data/interview_dataset_movies.csv')
      # need to convert string to list of floats
      self.df['vector_embedding'] = self.df['vector_embedding'].map(lambda s: ast.literal_eval(s))

    def query(self, query_vector: Embedding, min_age: int, max_age: int, count: int) -> List[MovieResponse]:
        df = self.df[(self.df['age'] >= min_age) & (self.df['age'] <= max_age) ]
        if type(df) == DataFrame:
            df['score'] = df['vector_embedding'].map(lambda vec: similarity_score (vec, query_vector))
            sorted_df = df.sort_values(by='score', ascending=False)
            # print(str(sorted_df.head(count)[['response_text', 'age', 'score']] ))
            columns = ['respondent_id', 'respondent_name', 'country', 'age', 'response_text']
            movies = sorted_df.head(count)[columns].apply(lambda row: MovieResponse(**row), axis=1).tolist()
            return movies
        return []
