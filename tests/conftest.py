import os
import sys
from pathlib import Path

import pytest
from betamax import Betamax
from flask_dance.consumer.storage import MemoryStorage
from flask_dance.contrib.github import github

toplevel = Path(__file__).parent.parent
sys.path.insert(0, str(toplevel))
from github import app as flask_app, github_bp


GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_OAUTH_ACCESS_TOKEN", "fake-token")

with Betamax.configure() as config:
    config.cassette_library_dir = toplevel / "tests" / "cassettes"
    config.define_cassette_placeholder("<AUTH_TOKEN>", GITHUB_ACCESS_TOKEN)


@pytest.fixture(autouse=True)
def github_storage(monkeypatch):
    """
    Monkeypatch the GitHub Flask-Dance blueprint so that the
    OAuth token is always set.
    """
    storage = MemoryStorage({"access_token": GITHUB_ACCESS_TOKEN})
    monkeypatch.setattr(github_bp, "storage", storage)
    return storage


@pytest.fixture
def app():
    return flask_app


@pytest.fixture
def flask_dance_sessions():
    """
    Necessary to use the ``betamax_record_flask_dance`` fixture
    from Flask-Dance
    """
    return github
