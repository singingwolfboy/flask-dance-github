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
def app(request):
    """
    Wraps the Flask app with `before_request` and `after_request` functions
    which activate Betamax on the `github` Flask-Dance session
    during incoming HTTP requests.
    """

    @flask_app.before_request
    def wrap_github_with_betamax():
        recorder = Betamax(
            github, cassette_library_dir=toplevel / "tests" / "cassettes"
        )
        recorder.use_cassette(request.node.name)
        recorder.start()

        @flask_app.after_request
        def unwrap(response):
            recorder.stop()
            return response

        request.addfinalizer(lambda: flask_app.after_request_funcs[None].remove(unwrap))

    request.addfinalizer(
        lambda: flask_app.before_request_funcs[None].remove(wrap_github_with_betamax)
    )

    return flask_app
