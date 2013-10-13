from setuptools import setup

import remarkable

setup(
    name=remarkable.__name__,
    version=remarkable.__version__,
    description='remarkable',
    author='Michael Joseph',
    author_email='michaeljoseph@gmail.com',
    url=remarkable.__url__,
    packages=['remarkable'],
    package_dir={'remarkable': 'remarkable'},
    include_package_data=True,
    install_requires=[
        'docopt < 1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'remarkable = remarkable.cli:main',
        ],
    },
    test_suite='nose.collector',
    license=open('LICENSE').read(),
)
