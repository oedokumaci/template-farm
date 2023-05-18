from pathlib import Path
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from template_farm.api import app
from template_farm.path import ROOT_DIR


# Fixture for paths
@pytest.fixture(
    params=[ROOT_DIR],
    ids=["root_dir"],
)
def path(request: pytest.FixtureRequest) -> Generator[Path, None, None]:
    """A fixture that provides a path for testing.

    This fixture takes a request parameter, which is used to parametrize the fixture
    with different paths. The fixture yields the path corresponding to the request
    parameter. The fixture is used to provide paths to the test functions.
    """
    yield request.param


@pytest.fixture
def client() -> TestClient:
    """
    Pytest fixture that provides a TestClient instance for testing the FastAPI app.

    Returns:
        TestClient: An instance of TestClient configured for the FastAPI app.
    """
    return TestClient(app)
