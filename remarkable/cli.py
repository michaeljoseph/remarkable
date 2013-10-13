"""
remarkable.

Usage:
  remarkable [options] remark <path-to-markdown-file>

  remarkable -h | --help

Options:
  --debug               Debug.

  -h --help             Show this screen.
"""
import logging

from docopt import docopt
from jinja2 import Environment, PackageLoader

import remarkable

log = logging.getLogger(__name__)


def render_template(template_name, context):
    return Environment(
        loader=PackageLoader('remarkable', 'templates')
    ).get_template(template_name).render(context)


def remark(arguments):
    file_name = arguments['<path-to-markdown-file>']
    html_file_name = '%s.html' % file_name

    html = render_template(
        'remark.html',
        dict(markdown=open(file_name).read())
    )
    with open(html_file_name, 'w') as html_file:
        html_file.write(html)
    log.info('Created %s' % html_file_name)


def main():
    arguments = docopt(__doc__, version=remarkable.__version__)

    logging.basicConfig(
        level=logging.DEBUG if arguments['--debug'] else logging.INFO
    )
    log.debug('arguments: %s', arguments)
    if arguments['remark']:
        remark(arguments)
