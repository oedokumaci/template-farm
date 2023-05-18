from fastapi.testclient import TestClient

from template_farm.api import app


def test_read_root() -> None:
    """
    Test function to verify the behavior of the root endpoint ("/").

    Returns:
        None
    """
    with TestClient(app, base_url="http://0.0.0.0:8000") as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
