#!/usr/bin/env python

import click

from .scrape import scrape

@click.group()
def cli():
    pass


@click.command(
    short_help='Set required parameters to bypass bot blocker'
)
@click.option(
    '-a',
    '--agent',
    help='The user agent name of your browser',
    prompt=True,
)
@click.option(
    '-c',
    '--cookie',
    help='The cookie generated from your browser',
    prompt=True,
)
def setup(agent, cookie):
    print(agent, cookie)


@click.command(
    short_help='Get earnings history for the ticker symbol'
)
@click.option(
    '-o',
    '--outfile',
    type=click.Path(),
    help='Output file to save earnings history',
)
@click.argument(
    'symbol',
)
def ticker(outfile, symbol):
    earnings = scrape(symbol)
    print(earnings)

    if outfile:
        earnings.to_csv(outfile, index=False)


cli.add_command(setup)
cli.add_command(ticker)

if __name__ == '__main__':
    cli()