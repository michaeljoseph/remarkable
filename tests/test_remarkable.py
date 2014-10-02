import io
import sys
import logging
import os
import shutil

from remarkable import cli
from . import BaseTestCase


log = logging.getLogger(__name__)


class TestRemarkTestCase(BaseTestCase):

    def test_remark(self):
        presentation_index = 'application-to-platform/index.html'
        sys.argv = [
            'remarkable',
            'remark',
            self.example_file,
            self.title,
        ]
        cli.main()
        self.assertTrue(os.path.exists(presentation_index))
        presentation_contents = io.open(presentation_index).read()
        self.assertTrue(self.title in presentation_contents)
        log.debug(presentation_contents)
        self.assertTrue('michaeljoseph' in presentation_contents)
        shutil.rmtree('application-to-platform')


class TestRevealTestCase(BaseTestCase):

    def test_reveal(self):
        presentation_index = 'application-to-platform/index.html'
        sys.argv = [
            'remarkable',
            'reveal',
            self.example_file,
            self.title,
        ]
        cli.main()
        self.assertTrue(os.path.exists(presentation_index))
        self.assertTrue(self.title in io.open(presentation_index).read())
        shutil.rmtree('application-to-platform')
