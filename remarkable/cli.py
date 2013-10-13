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


def main():
    arguments = docopt(__doc__, version=remarkable.__version__)
    debug = arguments['--debug']
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    log.debug('arguments: %s', arguments)

    if arguments['remark']:
        file_name = arguments['<path-to-markdown-file>']
        html_file_name = '%s.html' % file_name

        html = render_remark(open(file_name).read())
        with open(html_file_name, 'w') as html_file:
            html_file.write(html)
        log.info('Created %s' % html_file_name)


def render_remark(markdown):
    loader = PackageLoader('remarkable', 'templates')
    env = Environment(loader=loader)
    template = env.get_template('remark.html')
    return template.render({'markdown': markdown})
