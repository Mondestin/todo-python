from fastapi.testclient import TestClient
from main import app
import pytest

# Create a TestClient instance for making HTTP requests
client = TestClient(app)

# Test case for creating a user successfully
def test_create_user_success():
    res = client.post("/auth/signup", json={
        "email": "test.user1@gmail.com", "password": "password"
    })
    assert res.status_code == 201

# Test case for creating a user with a conflicting email address
def test_create_user_conflict(create_user):
    conflicting_email = "test@gmail.com"
    res = client.post("/auth/signup", json={
        "email": conflicting_email, 'password': "password"
    })
    assert res.status_code == 409
