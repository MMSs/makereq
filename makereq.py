#!/usr/bin/env python
import click, requests

@click.command()
@click.option('--count', '-c', default=1, help='Count of requests to generate.')
@click.option('--url', '-u', prompt='URL to make request to',
              help='The URL to generate requests to.')
@click.option('--get', 'method', flag_value='get', help='Generate a GET request.')
@click.option('--post', 'method', flag_value='post', help='Generate a POST request.')
@click.option('--method', '-m', type=click.Choice(['get', 'post']), default='get',
              help='Method to use to generate the request')
@click.option('--params', '-p', default='', multiple=True, help='Request parameters to be appended')
def makereq(count, url, method, params):
    """Simple program that generates requests to a URL a number of times."""
    statuses = []
    for x in range(count):
        if method == 'post':
            r = requests.post(url, params=params)
        else:
            r = requests.get(url, params=params)
        statuses.append([(r.url, r.status_code, r.elapsed)])
    return statuses

if __name__ == '__main__':
    print makereq()