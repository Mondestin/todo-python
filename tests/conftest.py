from firebase_admin import auth
from fastapi.testclient import TestClient
from main import app
import pytest
import os
os.environ['TESTING'] = 'True'

# Create a TestClient instance
client = TestClient(app)

# Define a fixture to clean up resources after testing
@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    def remove_test_users():
        users = auth.list_users().iterate_all()
        for user in users:
            if user.email.startswith("test."):
                auth.delete_user(user.uid)
    request.addfinalizer(remove_test_users)

# Define a fixture to create a test user during testing
@pytest.fixture
def create_user():
    user_credential = client.post("/auth/signup", json={
        "email": "test@gmail.com", 'password': "12345678"
    })

# Define a fixture to authenticate a test user during testing
@pytest.fixture
def auth_user(create_user):
    user_credential = client.post("/auth/login", data={
        "username": "test@gmail.com",
        "password": "12345678",
    })
    return user_credential.json()

# Define fixture to create a sample Todo for testing
@pytest.fixture
def create_sample_todo():
    sample_todo_data = {"name": "Test Todo"}
    response = client.post("/todos/", json=sample_todo_data)
    return response.json()