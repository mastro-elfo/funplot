import click
from json import dump, load
import math
import pandas as pd

from .lib import load_config, store_config, update_config, save_figure, plot as plot_fn


# Command line intarface
@click.group()
def cli():
    pass


@cli.command(help="Draw a function graph")
# Function options
@click.option(
    "-f", "--function", default=None, multiple=True, help="The function to plot"
)
@click.option(
    "-ld", "--left-domain", default=None, type=float, help="Domain left limit"
)
@click.option(
    "-rd", "--right-domain", default=None, type=float, help="Domain right limit"
)
@click.option("--points", default=None, type=int, help="Number of points")
@click.option(
    "-ul", "--upper-limit", default=None, type=float, help="Function upper limit"
)
@click.option(
    "-ll", "--lower-limit", default=None, type=float, help="Function lower limit"
)
# Graph options
@click.option("-t", "--title", default=None, help="Graph title")
@click.option(
    "-va",
    "--vertical-asymptote",
    default=None,
    type=float,
    multiple=True,
    help="X of vertical asymptote",
)
@click.option(
    "-ha",
    "--horizontal-asymptote",
    default=None,
    type=float,
    multiple=True,
    help="Y of horizontal asymptote",
)
@click.option(
    "-oa",
    "--oblique-asymptote",
    default=None,
    multiple=True,
    type=(float, float),
    help="Slope and intercept of asymptote",
)
@click.option(
    "-p",
    "--point",
    default=None,
    multiple=True,
    type=(float, float),
    help="Point X and Y",
)
# Config file
@click.option("-if", "--input_file", default=None, help="Load config from file")
@click.option("-of", "--output-file", default=None, help="Dump config to file")
@click.option("--figure", default=None, help="File name for the plot")
def draw(figure, input_file, output_file, **config):
    # Filter None(s)
    config = {key: val for key, val in config.items() if val is not None and val != ()}
    # Load config
    from_file = load_config(input_file)
    # Update config
    update_config(config, from_file)
    # Plot
    plot = plot_fn(**config)
    # Save figure
    save_figure(figure, plot)
    # Store config
    store_config(output_file, config)


if __name__ == "__main__":
    cli()
