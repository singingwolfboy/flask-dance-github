Automated Tests
===============

To run the tests, you need to install two Python packages:
Pytest_ and Betamax_. You can install them with ``pip``, like this:

.. code-block: bash
    pip install pytest betamax

Then you can run the tests using the ``pytest`` command:

.. code-block: bash
    pytest

Fixtures
--------

The ``conftest.py`` file contains the Pytest fixtures that
the tests use. Notice how the ``app`` fixture wraps the Betamax
tool around the ``github`` session from Flask-Dance. This allows
the tests to record and replay HTTP requests.

Cassettes
---------

The ``cassettes`` directory contains recorded HTTP sessions,
which the automated tests can replay. To record new HTTP sessions,
delete the files in that directory, and then run the tests again.

When making live HTTP requests to GitHub, such as when you record
new HTTP sessions, you must have a valid OAuth token for GitHub.
Put this OAuth token in the ``GITHUB_OAUTH_ACCESS_TOKEN`` environment
variable, and the automated tests will automatically pick it up.

.. _Pytest: https://pytest.org/
.. _Betamax: https://betamax.readthedocs.io/
