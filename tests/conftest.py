import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    """Create a test client that skips service initialization."""
    from app.config import settings
    from main import app
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c
