"""CLI script for the test_3R package. This will be called on the command line"""

import click

from test_3R.test_3R import hello_world
from test_3R.test_3R import addone


@click.command()
@click.option("--message", default=None, help="Type a message to say")
@click.option(
    "--addone", "number", type=int, default=None, help="Add 1 to a number"
)
@click.version_option()
def test_3R_cli(message, number):
  """Example script. This function is referenced in setup.cfg"""
  if message is not None:
    click.echo(hello_world(message))
  if number is not None:
    click.echo(addone(number))
