import sys
import os

from remarkable import cli
from . import BaseTestCase


class TestRemarkTestCase(BaseTestCase):

    def test_remark(self):
        sys.argv = 'remarkable remark atp.md foo'.split(' ')
        cli.main()
        self.assertTrue(os.path.exists('%s.html' % self.example_file))


class TestRevealTestCase(BaseTestCase):

    def test_reveal(self):
        sys.argv = 'remarkable reveal atp.md foo'.split(' ')
        cli.main()
        self.assertTrue(os.path.exists('%s.html' % self.example_file))
