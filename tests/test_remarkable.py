import sys
import os

from remarkable import cli
from . import BaseTestCase


class TestRemarkTestCase(BaseTestCase):

    def test_remark(self):
        sys.argv = ('remarkable remark %s' % self.example_file).split(' ')
        cli.main()
        self.assertTrue(os.path.exists('remark.html'))


class TestRevealTestCase(BaseTestCase):
    title = 'application-to-platform'
    presentation_index = '%s/index.html' % title

    def test_reveal(self):
        sys.argv = [
            'remarkable',
            'reveal',
            self.example_file,
            self.title,
        ]
        cli.main()
        self.assertTrue(os.path.exists(self.presentation_index))

    def tearDown(self):
        super(TestRevealTestCase, self).tearDown()
        if os.path.exists(self.presentation_index):
            os.remove(self.presentation_index)
