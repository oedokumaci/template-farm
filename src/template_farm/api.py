import pathlib

import uvicorn
from fastapi import FastAPI

from template_farm.path import LOGS_DIR
from template_farm.utils import find_available_port

app = FastAPI()
log_file: pathlib.Path = LOGS_DIR / "api.log"


def run_server() -> None:
    """Run the FastAPI server."""
    log_file.unlink(missing_ok=True)
    log_config: pathlib.Path = LOGS_DIR / "logging.conf"
    port = find_available_port(8000, 9999)
    uvicorn.run(app, host="0.0.0.0", port=port, log_config=str(log_config))


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/logs")
def read_logs() -> str:
    with open(log_file) as f:
        return f.read()
