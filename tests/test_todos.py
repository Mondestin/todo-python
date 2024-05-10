from fastapi.testclient import TestClient
from main import app
from database.firebase import db
from classes.schema_dto import Todo, TodoNoID
import uuid
import pytest

# Create a TestClient instance for making HTTP requests
client = TestClient(app)

# Test case to get all todos
def test_get_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test case to create a new Todo
def test_create_todo():
    new_todo_data = {"name": "New Todo"}
    response = client.post("/todos/", json=new_todo_data)
    assert response.status_code == 201
    assert response.json()["name"] == "New Todo"

# Test case to get a Todo by ID
def test_get_todo_by_id(create_sample_todo):
    todo_id = create_sample_todo["id"]
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id


# Test case to get a Todo by ID that doesn't exist
def test_get_nonexistent_todo():
    nonexistent_id = str(uuid.uuid4()) 
    response = client.get(f"/todos/{nonexistent_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"


# Test case to modify an existing Todo's name
def test_modify_todo_name(create_sample_todo):
    todo_id = create_sample_todo["id"]
    updated_data = {"name": "Updated Todo"}
    response = client.patch(f"/todos/{todo_id}", json=updated_data)
    assert response.status_code == 204

# Test case to delete a Todo
def test_delete_todo(create_sample_todo):
    todo_id = create_sample_todo["id"]
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204
    assert db.child("todos").child(todo_id).get().val() is None
