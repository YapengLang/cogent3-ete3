from pathlib import Path

import click

from scitrack import CachingLogger


__author__ = "YOUR NAME"
__copyright__ = "Copyright 2016-2021, YOUR NAME"
__credits__ = ["YOUR NAME"]
__license__ = "BSD"
__version__ = "2020.6.5"  # A DATE BASED VERSION
__maintainer__ = "YOUR NAME"
__email__ = "YOUR@email"
__status__ = "alpha"


LOGGER = CachingLogger()


@click.group()
@click.version_option(__version__)  # add version option
def main():
    """docstring explains what your cl app does"""
    pass


# note that I often define reusable options in a central place
_verbose = click.option(
    "-v",
    "--verbose",
    count=True,
    help="is an integer indicating number of cl occurrences",
)

# you can define custom parsers / validators
def _parse_csv_arg(*args) -> list:
    return args[-1].split(",")


_names = click.option(
    "--names",
    callback=_parse_csv_arg,
    help="converts comma separated values",
)

_outpath = click.option(
    "-o", "--outpath", type=Path, help="the input string will be cast to Path instance"
)

# the no_args_is_help=True means help is displayed if a
# user doesn't provide any arguments to a subcommand.
# Should be a click default I think!
@main.command(no_args_is_help=True)
@click.option(
    "-i",
    "--infile",
    required=True,
    type=click.Path(exists=True),
    help="fails if provided value is non-existent path",
)
@_outpath
@click.option(
    "--achoice",
    type=click.Choice(["choice1", "choice2"]),
    default="choice1",
    help="make a choice",
)
@_names
@click.option(
    "-O",
    "--overwrite",
    is_flag=True,
    help="overwrite results",
)
@click.option(
    "--ensembl_account",
    envvar="ENSEMBL_ACCOUNT",
    help="shell variable with MySQL account "
    "details, e.g. export "
    "ENSEMBL_ACCOUNT='myhost.com jill jills_pass'",
)
@_verbose
def demo_log(infile, outpath, achoice, names, overwrite, verbose, ensembl_account):
    """what demo_log subcommand does"""
    # capture the local variables, at this point just provided arguments
    LOGGER.log_args()
    LOGGER.log_versions("numpy")
    LOGGER.input_file(infile)

    LOGGER.log_file_path = outpath / "some_path.log"


def _parse_csv_arg(*args):
    return args[-1].split(",")


@main.command(no_args_is_help=True)
@click.argument("message", required=True, type=str)
@click.option("-t", "--test", is_flag=True, help="test run")
@_verbose
def demo_echo(message, test, verbose):
    """what demo_echo subcommand does"""
    for _ in range(verbose):
        click.secho(message, fg="blue")


if __name__ == "__main__":
    main()
