"""Module for paths used in the project."""

from pathlib import Path

ROOT_DIR: Path = Path(__file__).parents[2].resolve().expanduser()

LOGS_DIR: Path = ROOT_DIR / "logs"
