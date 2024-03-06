import pandas as pd
import ast
from pandas import DataFrame
from domain import MovieResponse
from domain.contracts import IVectorStore
from domain.contracts import Embedding
from infra.embedding import EmbeddingService

# remove warning about updating df slice
pd.set_option('mode.chained_assignment', None)

class VectorStore(IVectorStore):
    columns = ['respondent_id', 'respondent_name', 'country', 'age', 'response_text','vector_embedding']
    df:DataFrame
    def __init__(self) -> None:
      self.df = pd.read_csv('./data/interview_dataset_movies.csv')
      # need to convert string to list of floats
      self.df['vector_embedding'] = self.df['vector_embedding'].map(lambda s: ast.literal_eval(s))

    def query(self, query_vector: Embedding, min_age: int, max_age: int) -> MovieResponse:
        df = self.df[(self.df['age'] >= min_age) & (self.df['age'] <= max_age) ]
        if type(df) == DataFrame:
          df['score'] = df['vector_embedding'].map(lambda vec: EmbeddingService.similarity(vec, query_vector))
          sorted_df = df.sort_values(by='score', ascending=False)
          print(str(sorted_df.head(10)[['response_text', 'respondent_id', 'score']] ))
        return MovieResponse(respondent_id=2,
                             respondent_name="some name",
                             country="some country",
                             age=22,
                             response_text="some response text",
                             vector_embedding=[1,2,3])

        # return MovieResponse(respondent_id=self.df['respondent_id'],
        #                      respondent_name=self.df[''],
        #                      country=self.df[''],
        #                      age=self.df[''],
        #                      response_text=self.df[''],
        #                      vecter_embedding=self.df[''])

