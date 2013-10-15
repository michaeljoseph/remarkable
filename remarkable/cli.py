"""
remarkable.

Usage:
  remarkable [options] remark <path-to-markdown-file> [<title>]
  remarkable [options] reveal <path-to-markdown-file> <title>

  remarkable -h | --help

Options:
  --debug               Debug.

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

log = logging.getLogger(__name__)


def render_template(template_name, context):
    return Environment(
        loader=PackageLoader('remarkable')
    ).get_template(template_name).render(context)


def ask(question):
    '''Display a Y/n question prompt, and return a boolean'''
    while True:
        print
        input_ = raw_input('%s [Y/n] ' % question)
        input_ = input_.strip().lower()
        if input_ in ('y', 'yes', ''):
            return True
        if input_ in ('n', 'no'):
            return False
        print('Invalid selection')


def render_template_directory(deck):
    output_directory = deck.title

    if os.path.exists(output_directory):
        if sys.stdout.isatty():
            if ask('%s already exists, shall I delete it?'):
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


def read_file(file_name):
    return open(file_name).read().decode('utf-8')


def write_file(file_name, content):
    with open(file_name, 'w') as html_file:
        html_file.write(content.encode('utf-8'))
    log.info('Created %s' % file_name)


def remark(arguments):
    html = render_template(
        'remark/index.html',
        dict(markdown=read_file(arguments['<path-to-markdown-file>'])),
    )

    title = arguments.get('<title>', 'Remark Presentation')
    write_file(
        '%s.html' % (title if title else 'remark'),
        html,
    )


def reveal(arguments):
    render_template_directory(Deck(
        arguments.get('<title>', 'Reveal Presentation'),
        read_file(arguments['<path-to-markdown-file>']),
        'reveal'
    ))


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
