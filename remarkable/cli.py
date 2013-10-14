"""
remarkable.

Usage:
  remarkable [options] remark <path-to-markdown-file>
  remarkable [options] reveal <path-to-markdown-file>

  remarkable -h | --help

Options:
  --debug               Debug.

  -h --help             Show this screen.
"""
import logging

from docopt import docopt
from jinja2 import Environment, PackageLoader
from snide import Deck

import remarkable

log = logging.getLogger(__name__)


def render_template(template_name, context):
    return Environment(
        loader=PackageLoader('remarkable')
    ).get_template(template_name).render(context)


def read_file(file_name):
    return open(file_name).read().decode('utf-8')


def write_file(file_name, content):
    with open(file_name, 'w') as html_file:
        html_file.write(content.encode('utf-8'))
    log.info('Created %s' % file_name)


def remark(arguments):
    file_name = arguments['<path-to-markdown-file>']
    html = render_template(
        'remark.html',
        dict(markdown=read_file(file_name)),
    )
    write_file('%s.html' % file_name, html)


def reveal(arguments):
    file_name = arguments['<path-to-markdown-file>']
    deck = Deck('title', read_file(file_name))

    html = render_template(
        'reveal.html',
        dict(slides=deck.slides),
    )
    write_file('%s.html' % file_name, html)


def main():
    arguments = docopt(__doc__, version=remarkable.__version__)

    logging.basicConfig(
        level=logging.DEBUG if arguments['--debug'] else logging.INFO
    )
    log.debug('arguments: %s', arguments)

    commands = ['remark', 'reveal']
    for command in commands:
        if arguments[command]:
            globals()[command](arguments)

    if arguments['remark']:
        remark(arguments)
