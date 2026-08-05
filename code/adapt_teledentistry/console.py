from __future__ import annotations

from pathlib import Path

import typer

from .io import load_cases

app = typer.Typer(no_args_is_help=True)


@app.command()
def validate_data(path: Path) -> None:
    cases = load_cases(path)
    identifiers = [case.case_id for case in cases]
    if len(identifiers) != len(set(identifiers)):
        raise typer.BadParameter("case identifiers must be unique")
    typer.echo(f"validated {len(cases)} cases")


@app.command()
def describe() -> None:
    typer.echo("ADAPT six-agent dental emergency triage evaluation package")


if __name__ == "__main__":
    app()
