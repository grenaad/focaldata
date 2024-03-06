import typer
from typing_extensions import Annotated
from application import Application
from infra.embedding import EmbeddingService
from infra.store import VectorStore


OPENAI_KEY = "some key"

application = Application(EmbeddingService(OPENAI_KEY), VectorStore())

app = typer.Typer()

@app.command()
def search(
    query: Annotated[str, typer.Argument()],
    min_age: Annotated[int, typer.Option(min=0)] = 0,
    max_age: Annotated[int, typer.Option(min=0)] = 1000,
):
    application.search(query, min_age, max_age)


if __name__ == "__main__":
    app()
