from io import open
import logging

log = logging.getLogger(__name__)


def read_file(file_name, encoding='utf-8'):
    return open(file_name, encoding=encoding).read()


def write_file(file_name, content, encoding='utf-8'):
    with open(file_name, 'w', encoding=encoding) as output_file:
        output_file.write(content)
    log.info('Created %s' % file_name)
