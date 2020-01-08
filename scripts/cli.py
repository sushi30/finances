import click
from scripts.parse_credit_card import inner


@click.group()
def cli():
    pass


def decorate(f):
    for dec in [
        click.argument("path", type=click.File(mode="rb")),
        click.option("--out", default=None),
        click.option("--storage", default=None),
        cli.command(),
    ]:
        f = dec(f)
    return f


@decorate
def isracard(out, storage, path):
    inner("isracard", path, out, storage)


@decorate
def leumicard(out, storage, path):
    inner("leumicard", path, out, storage)


if __name__ == "__main__":
    cli()
