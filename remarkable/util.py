import logging

log = logging.getLogger(__name__)


def read_file(file_name, encoding='utf-8'):
    return open(file_name).read().decode(encoding)


def write_file(file_name, content, encoding='utf-8'):
    with open(file_name, 'w') as output_file:
        output_file.write(content.encode(encoding))
    log.info('Created %s' % file_name)
