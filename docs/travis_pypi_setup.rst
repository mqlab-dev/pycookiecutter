.. _travis-pypi-setup:


Travis/PyPI Setup
=================

Optionally, your package can automatically be released on PyPI whenever you
push a new tag to the master branch.

Install the Travis CLI tool
--------------------------------------

This is OS-specific.

### Mac OS X

We recommend the Homebrew travis package:

.. code-block:: bash

    brew install travis


### Windows and Linux

Follow the official Travis CLI installationinstructions for your operating system:

https://github.com/travis-ci/travis.rb#installation

How It Works
------------

Once you have the `travis` command - line tool installed, from the root of your project do::

    travis encrypt --add deploy.password

This will encrypt your locally-stored PyPI password and save that to your `.travis.yml` file. Commit that change to git.


More Details
------------

You can read more about using Travis for PyPI deployment at:
https://docs.travis-ci.com/user/deployment/pypi/
