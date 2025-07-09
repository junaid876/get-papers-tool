import typer
import pandas as pd
from get_papers_tool.pubmed_fetcher import search_pubmed, fetch_details

app = typer.Typer()

@app.command()
def get_papers_list(query: str, file: str = "", debug: bool = False):
    if debug:
        typer.echo(f"Searching for papers with query: {query}")

    ids = search_pubmed(query)
    if debug:
        typer.echo(f"Found {len(ids)} IDs")

    data = fetch_details(ids)

    df = pd.DataFrame(data)

    if file:
        df.to_csv(file, index=False)
        typer.echo(f"Saved to {file}")
    else:
        typer.echo(df.to_string())

if __name__ == "__main__":
    app()