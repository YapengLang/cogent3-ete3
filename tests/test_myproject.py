from pathlib import Path

import pytest

from click.testing import CliRunner

from myproject.cli import demo_echo, demo_log


DATADIR = Path(__file__).parent / "data"


@pytest.fixture(scope="session")
def tmp_dir(tmpdir_factory):
    return tmpdir_factory.mktemp("demo")


@pytest.fixture(scope="session")
def runner():
    """exportrc works correctly."""
    return CliRunner()


def test_demo_echo(tmp_dir, runner):
    args = "'hello!' -vv".split()
    r = runner.invoke(demo_echo, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output


def test_demo_log(tmp_dir, runner):
    args = f"-i {DATADIR / 'demo.fasta'} --names human,chimp -o {tmp_dir}".split()
    r = runner.invoke(demo_log, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output
