from unittest2 import TestCase


class BaseTestCase(TestCase):

    def setUp(self):
        self.example_file = 'atp.md'
        with open(self.example_file, 'w') as f:
            f.write(MARKDOWN)

    def tearDown(self):
        os.remove(self.example_file)
        os.remove('%s.html' % self.example_file)
