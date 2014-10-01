"""
remarkable.

Usage:
  remarkable [options] remark <path-to-markdown-file> [<title>]
  remarkable [options] reveal <path-to-markdown-file> <title>

  remarkable -h | --help

Options:
  --debug               Debug.
  --noinput             What it says.

  -h --help             Show this screen.
"""
import logging
import os
import shutil
import sys

from docopt import docopt
from jinja2 import Environment, PackageLoader
from snide import Deck

import remarkable
from .util import write_file, read_file

log = logging.getLogger(__name__)


def render_template(template_name, context):
    """Render a jinja template"""
    return Environment(
        loader=PackageLoader('remarkable')
    ).get_template(template_name).render(context)


def ask(question, no_input=False):
    """Display a Y/n question prompt, and return a boolean"""
    if no_input:
        return True
    else:
        input_ = raw_input('%s [Y/n] ' % question)
        input_ = input_.strip().lower()
        if input_ in ('y', 'yes', ''):
            return True
        if input_ in ('n', 'no'):
            return False
        print('Invalid selection')


def render_template_directory(deck, arguments):
    """Render a template directory"""
    output_directory = deck.title

    if os.path.exists(output_directory):
        if sys.stdout.isatty():
            if ask(
                '%s already exists, shall I delete it?' % output_directory,
                arguments.get('--noinput')
            ):
                shutil.rmtree(output_directory)
        else:
            shutil.rmtree(output_directory)

    # copy support files to output directory
    template_directory_path = (
        '%s/templates/%s' %
        (remarkable.__path__[0], deck.presentation_type)
    )
    shutil.copytree(
        template_directory_path,
        output_directory,
    )

    # write index to output directory
    write_file(
        '%s/index.html' % output_directory,

        render_template(
            '%s/index.html' % deck.presentation_type,
            dict(slides=deck.slides),
        ),
    )

    return output_directory


def file_name_from_title(title):
    return '%s.html' % '-'.join([word.lower() for word in title.split(' ')])


def remark(arguments):
    title = arguments.get('<title>', 'Remark Presentation')
    markdown_file = arguments['<path-to-markdown-file>']
    html = render_template(
        'remark/index.html', {
            'markdown': read_file(markdown_file),
            'title': title,
        }
    )
    write_file(file_name_from_title(title), html)


def reveal(arguments):
    render_template_directory(
        Deck(
            arguments.get('<title>', 'Reveal Presentation'),
            read_file(arguments['<path-to-markdown-file>']),
            'reveal'
        ),
        arguments,
    )


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
