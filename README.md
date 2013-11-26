# remarkable

[![Build Status](https://secure.travis-ci.org/michaeljoseph/remarkable.png)](http://travis-ci.org/michaeljoseph/remarkable)
[![Stories in Ready](https://badge.waffle.io/michaeljoseph/remarkable.png?label=ready)](https://waffle.io/michaeljoseph/remarkable) [![pypi version](https://badge.fury.io/py/remarkable.png)](http://badge.fury.io/py/remarkable)
[![# of downloads](https://pypip.in/d/remarkable/badge.png)](https://crate.io/packages/remarkable?version=latest)
[![code coverage](https://coveralls.io/repos/michaeljoseph/remarkable/badge.png?branch=master)](https://coveralls.io/r/michaeljoseph/remarkable?branch=master)

![remarkable](https://github.com/michaeljoseph/remarkable/raw/master/resources/remarkable.jpg)

## Overview

A mashup of http://lab.hakim.se/reveal-js and http://remarkjs.com

* CLI that processes a MarkDown file and emits an HTML presentation

## Usage

Install `remarkable`:

    pip install remarkable

## CLI

Run the cli:

```
remarkable.

Usage:
  remarkable [options] remark <path-to-markdown-file> [<title>]
  remarkable [options] reveal <path-to-markdown-file> <title>

  remarkable -h | --help

Options:
  --debug               Debug.

  -h --help             Show this screen.
```

Example:
```
$ remarkable remark application-to-platform.md
INFO:remarkable.cli:Created remark.html

$ remarkable reveal application-to-platform.md application-to-platform
INFO:remarkable.cli:Created application-to-platform/index.html
```

## Documentation

[API Documentation](http://remarkable.rtfd.org)

## Testing

Install development requirements:

    pip install -r requirements.txt

Tests can then be run with:

    nosetests

Lint the project with:

    flake8 changes tests

## API documentation

Generate the documentation with:

    cd docs && PYTHONPATH=.. make singlehtml

To monitor changes to Python files and execute flake8 and nosetests
automatically, execute the following from the root project directory:

    stir
