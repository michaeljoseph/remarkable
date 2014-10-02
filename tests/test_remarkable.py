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
        sys.argv = [
            'remarkable',
            'remark',
            self.example_file,
            self.title,
        ]
        cli.main()
        self.assertTrue(os.path.exists(self.presentation_index))
        presentation_contents = io.open(self.presentation_index).read()
        self.assertTrue(self.title in presentation_contents)
        shutil.rmtree(self.directory_name)


class TestRevealTestCase(BaseTestCase):

    def test_reveal(self):
        sys.argv = [
            'remarkable',
            'reveal',
            self.example_file,
            self.title,
        ]
        cli.main()
        self.assertTrue(os.path.exists(self.presentation_index))
        presentation_contents = io.open(self.presentation_index).read()
        self.assertTrue(self.title in presentation_contents)
        shutil.rmtree(self.directory_name)
