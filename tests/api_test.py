from fastapi.testclient import TestClient


def test_read_root(test_client: TestClient) -> None:
    """
    Test function to verify the behavior of the root endpoint ("/").

    Returns:
        None
    """
    with test_client as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
