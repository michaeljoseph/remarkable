import sys
import os

from remarkable import cli
from . import BaseTestCase


MARKDOWN = """
name: inverse
layout: true
class: center, middle, inverse
---
# Application To Platform
.footnote[
    [How we used Python to scale Yola]
    (https://github.com/michaeljoseph/application-to-platform)
]
---
layout: false
background-image: url(https://raw.github.com/michaeljoseph/images/yola.png)
.large[
![avatar](https://raw.github.com/michaeljoseph/images/avatar.png)
michaeljoseph   @github     @twitter
]
???
.small[
# excuses

- false pretences:  backup speaker

- 4 day talk

- crappy slides: squirrel (show remark / reveal)

- we're hiring, let me convince you / swimming the recruitment and
hiring manager infested nerdpool during the break
we have business cards
]
---
"""


class TestRemarkable(BaseTestCase):

    def setUp(self):
        self.example_file = 'atp.md'
        with open(self.example_file, 'w') as f:
            f.write(MARKDOWN)

    def tearDown(self):
        os.remove(self.example_file)
        os.remove('%s.html' % self.example_file)

    def test_remark(self):
        sys.argv = 'remarkable remark atp.md'.split(' ')
        cli.main()
        self.assertTrue(os.path.exists('%s.html' % self.example_file))
