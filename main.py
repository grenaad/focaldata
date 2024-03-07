import typer
from typing_extensions import Annotated
from application import Application
from infra.embedding import EmbeddingService
from infra.store import VectorStore
import configparser

application: Application

app = typer.Typer()

@app.command()
def search(
    query: Annotated[str, typer.Argument()],
    min_age: Annotated[int, typer.Option(min=0)] = 0,
    max_age: Annotated[int, typer.Option(min=0)] = 1000,
):
    application.search(query, min_age, max_age)

def read_config(section, key):
    try:
      config = configparser.ConfigParser()
      config.read('config.ini')
      return config[section][key]
    except Exception:
      return None

if __name__ == "__main__":
    openai_key = read_config('LOGIN', 'openai_key')
    if openai_key == None:
        print("Error: no OpenAI key provided")
    else:
      application = Application(EmbeddingService(openai_key), VectorStore())
      app()

