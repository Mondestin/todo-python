from fastapi.testclient import TestClient
from main import app

# Create a TestClient instance
client = TestClient(app)

# Define a test for the main endpoint ("/")
def test_docs():
    res = client.get("/docs")
    assert res.status_code == 200

# Define a test for the Redoc documentation endpoint 
def test_redoc():
    res = client.get("/redoc")
    assert res.status_code == 200
