import textwrap


import click
import requests


from . import __version__

API_URL = "https://pt.wikipedia.org/api/rest_v1/page/summary/Índice_de_massa_corporal"


def get_imc_page():
    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)

def get_imc_from_user(weight: int, height: float) -> float:
    """
        input:
            weight -> user weight in kg
            height -> user height in meters
        output:
            imc -> user's imc
    """
    return round( weight / (height * height), 2 )

@click.command()
@click.option(
    "--weight",
    "-w",
    default="64",
    help="Your weight",
    metavar="WEIGHT",
    show_default=True,
)
@click.option(
    "--height",
    "-h",
    default="1",
    help="Your height",
    metavar="HEIGHT",
    show_default=True,
)
@click.version_option(version=__version__)
def main(weight, height):
    """The hypermodern imc project."""
    data = get_imc_page()
    imc = get_imc_from_user(int(weight), float(height))
    
    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
    click.secho("Seu IMC é {}!".format(imc), fg="blue")