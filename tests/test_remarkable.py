import io
import sys
import os
import shutil

from remarkable import cli
from . import BaseTestCase


class TestRemarkTestCase(BaseTestCase):

    def test_remark(self):
        cmd_line = 'remarkable remark %s %s' % (self.example_file, self.title)
        sys.argv = cmd_line.split(' ')
        cli.main()
        self.assertTrue(os.path.exists('application-to-platform.html'))
        os.remove('application-to-platform.html')


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
