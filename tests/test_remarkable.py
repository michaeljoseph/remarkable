from . import BaseTestCase

from remarkable import remarkable


class TestRemarkable(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            remarkable(),
        )
