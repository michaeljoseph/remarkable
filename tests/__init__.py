import os

from unittest2 import TestCase

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


class BaseTestCase(TestCase):
    title = 'Application To Platform'
    directory_name = 'application-to-platform'
    example_file = 'atp.md'

    def setUp(self):
        with open(self.example_file, 'w') as f:
            f.write(MARKDOWN)

    def tearDown(self):
        os.remove(self.example_file)
        for filename in ['%s.html' % self.example_file, 'remark.html']:
            if os.path.exists(filename):
                os.remove(filename)
