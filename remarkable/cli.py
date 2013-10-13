"""
remarkable.

Usage:
  remarkable [options] command <param> <another_params>
  remarkable [options] another-command <param>

  remarkable -h | --help

Options:
  --kw-arg=<kw>         Keyword option description.
  -b --boolean          Boolean option description.
  --debug               Debug.

  -h --help             Show this screen.
"""

from docopt import docopt
import logging

import remarkable

log = logging.getLogger(__name__)


def main():
    arguments = docopt(__doc__, version=changes.__version__)
    debug = arguments['--debug']
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    log.debug('arguments: %s', arguments)
