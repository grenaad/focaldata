import typer
from typing_extensions import Annotated
from application import Application
from infra import EmbeddingService


OPENAI_KEY = "some key"

application = Application(EmbeddingService(OPENAI_KEY))

app = typer.Typer()

@app.command()
def search(
    min_age: Annotated[int, typer.Option(min=0)] = 0,
    max_age: Annotated[int, typer.Option(min=0)] = 1000,
):
    application.search(min_age, max_age)


if __name__ == "__main__":
    app()
