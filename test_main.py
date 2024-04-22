from fastapi.testclient import TestClient

from .main import app, todos

client = TestClient(app)

# Wrtie all the test cases here in this file for every functionality need to be tested.


# Clearing the list by default.
def setup_function():
    todos.clear()

# Test case for getting and reading all the todos from the array object.
def test_read_todos():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []

# Test case for creating a new todo is it is passed or not.
def test_create_todo():
    response = client.post("/", json={"name": "Buy groceries", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"name": "Buy groceries", "completed": False}


# Test case for getting and reading single todo.
def test_read_todo():
    client.post("/", json={"name": "Buy groceries", "completed": False})
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Buy groceries", "completed": False}


# Test case for updating single todo.
def test_update_todo():
    client.post("/", json={"name": "Buy groceries", "completed": False})
    response = client.put("/1", json={"name": "Buy vegetables", "completed": True})
    assert response.status_code == 200
    assert response.json() == {"name": "Buy vegetables", "completed": True}
    


# Test case for deleting single todo.
def test_delete_todo():
    client.post("/", json={"name": "Buy groceries", "completed": False})
    response = client.delete("/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Buy groceries", "completed": False}
