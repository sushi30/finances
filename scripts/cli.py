import click
from scripts.parse_credit_card import inner


@click.group()
@click.option("--out", default=None)
@click.option("--storage", default=None)
@click.pass_context
def cli(ctx, **kwargs):
    ctx.obj = kwargs


@cli.command()
@click.argument("path", type=click.File(mode="rb"))
@click.pass_context
def isracard(ctx, path):
    inner("isracard", path, ctx.obj["out"], ctx.obj["storage"])


@cli.command()
@click.argument("path", type=click.File(mode="rb"))
@click.pass_context
def leumicard(ctx, path):
    inner("leumicard", path, ctx.obj["out"], ctx.obj["storage"])


if __name__ == "__main__":
    cli()
