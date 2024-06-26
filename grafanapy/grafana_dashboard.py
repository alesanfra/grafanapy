from pathlib import Path

import typer

from grafanapy import converter

app = typer.Typer()


@app.command()
def json_to_python(
    json_path: Path = typer.Option(...),
    python_path: Path = typer.Option(...),
):
    converter.json_to_python.convert(
        json_path=json_path,
        python_path=python_path,
    )


@app.command()
def python_to_json(
    python_base_dir: Path = typer.Option(...),
    python_base_package: str = typer.Option(...),
    json_dir: Path = typer.Option(...),
):
    converter.python_to_json.convert_package(
        python_base_dir=python_base_dir,
        python_base_package=python_base_package,
        json_dir=json_dir,
    )


# https://github.com/tiangolo/typer/issues/34
def run():
    app()


if __name__ == "__main__":
    run()
