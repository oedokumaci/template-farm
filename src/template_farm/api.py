import logging

import uvicorn
from fastapi import FastAPI

from template_farm.utils import init_logger

app = FastAPI()


def run_server(port: int = 8000) -> None:
    """Run the FastAPI server."""
    # Initialize logger
    init_logger("api.log")

    logging.info(f"Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}
