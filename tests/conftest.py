import logging
from pathlib import Path
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from template_farm.api import app
from template_farm.path import LOGS_DIR, ROOT_DIR
from template_farm.utils import init_logger

# Path to the log file to be used for testing
pytest_log_file: Path = LOGS_DIR / "pytest_test.log"


# Fixture to handle cleanup process for all fixtures
@pytest.fixture
def cleanup() -> Generator[None, None, None]:
    """A fixture that performs cleanup after each test function.

    This fixture is responsible for cleaning up all fixtures by closing all the handlers
    of the logger and deleting the log file. The fixture is used as a yield fixture
    that is called after the execution of the test function completes.
    """
    yield
    for handler in logging.getLogger().handlers:  # close all handlers, Windows fix
        handler.close()
    pytest_log_file.unlink()


# Fixture to set up logger for tests
@pytest.fixture
def logger_fixture(cleanup: Generator[None, None, None]) -> Generator[None, None, None]:
    """A fixture that sets up the logger for testing.

    This fixture sets up the logger by initializing it with the log file to be used for
    testing. The fixture is used as a yield fixture that is called before the execution
    of the test function starts.
    """
    init_logger(pytest_log_file.name)
    yield


# Fixture for paths
@pytest.fixture(
    params=[ROOT_DIR, LOGS_DIR],
    ids=["root_dir", "logs_dir"],
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
