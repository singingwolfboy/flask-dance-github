Automated Tests
===============

To run the tests, you need to install two Python packages:
Pytest_ and Betamax_. You can install them with ``pip``, like this:

.. code-block:: bash

    pip install pytest betamax

Then you can run the tests using the ``pytest`` command:

.. code-block:: bash

    pytest

Fixtures
--------

The ``conftest.py`` file contains the `Pytest fixtures`_ that
the tests use. We want to use the ``betamax_record_flask_dance``
fixture `provided by Flask-Dance
<https://flask-dance.readthedocs.io/en/latest/testing.html#module-flask_dance.fixtures.pytest>`_,
so we define an ``app`` fixture and a ``flask_dance_sessions``
fixture. We also define a ``github_authorized`` fixture,
which will use a ``MemoryStorage`` object to tell Flask-Dance
that the user is already authorized with GitHub.

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
.. _Pytest fixtures: https://docs.pytest.org/en/latest/fixture.html
