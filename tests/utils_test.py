import logging
from typing import Generator

import pytest
from pytest import LogCaptureFixture

from template_farm.path import LOGS_DIR
from template_farm.utils import timer_decorator


@pytest.mark.parametrize(
    "level,msg",
    [
        (logging.INFO, "info"),
        (logging.WARNING, "warning"),
        (logging.ERROR, "error"),
        (logging.CRITICAL, "critical"),
    ],
)
def test_init_logger(
    logger_fixture: Generator[None, None, None],
    caplog: LogCaptureFixture,
    level: int,
    msg: str,
) -> None:
    """Test if the logger object is initialized and produces the correct log messages.

    This test function checks if the logger object is initialized correctly and if it
    produces the correct log messages. The function takes the logger_fixture, which sets
    up the logger, the caplog fixture, which is used to capture the log messages, the
    logging level, and the log message.

    Args:
        logger_fixture (Generator[None, None, None]): The logger fixture.
        caplog (LogCaptureFixture): The fixture to capture log messages.
        level (int): The logging level.
        msg (str): The log message.

    Returns:
        None
    """
    logger_fixture

    # Assert that the log file was created in the correct directory
    log_file_path = LOGS_DIR / "pytest_test.log"
    assert log_file_path.is_file()

    # Log a message at the specified level
    logging.log(level, msg)

    # Assert that the correct logs were produced
    assert caplog.record_tuples[-1] == ("root", level, msg)


def test_timer_decorator(
    caplog: LogCaptureFixture, cleanup: Generator[None, None, None]
) -> None:
    """Test if the timer_decorator function correctly times the execution of a function.

    This test function checks if the timer_decorator function correctly times the
    execution of a function. The function takes the caplog fixture, which is used to
    capture the log messages, and the cleanup fixture to handle cleanup process for the logger.

    Args:
        caplog (LogCaptureFixture): The fixture to capture log messages.
        cleanup (Generator[None, None, None]): The fixture to handle cleanup process for the logger.

    Returns:
        None
    """

    # Define a test function that takes some time to execute
    @timer_decorator
    def test_function() -> str:
        for _ in range(1000000):
            pass
        return "done"

    # Call the function and check that the correct logs were produced
    result = test_function()
    assert result == "done"
    assert caplog.record_tuples[0][2].startswith(
        "Method 'test_function' of module 'tests.utils_test' executed in "
    )
