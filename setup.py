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
        'Jinja2 < 3.0.0',
        'docopt < 1.0.0',
        'snide < 1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'remarkable = remarkable.cli:main',
        ],
    },
    test_suite='nose.collector',
    license=open('LICENSE').read(),
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
