import pytest
from src.app import app, todos

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clear_todos():
    todos.clear()  # Rensar listan innan varje test


def test_index(client):
    """Test that index page loads correctly"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Min Todo-lista' in rv.data

def test_add_todo(client):
    """Test adding a todo item"""
    rv = client.post('/add', data={'todo': 'Test uppgift'})
    assert rv.status_code == 302  # Redirect
    
    rv = client.get('/')
    assert b'Test uppgift' in rv.data

def test_toggle_todo(client):
    """Test toggling a todo item"""
    # First add a todo
    client.post('/add', data={'todo': 'Toggle test'})
    
    # Then toggle it
    rv = client.get('/toggle/0')
    assert rv.status_code == 302  # Redirect

def test_delete_todo(client):
    """Test deleting a todo item"""
    # First add two todos
    client.post('/add', data={'todo': 'Delete test'})
    client.post('/add', data={'todo': 'Another task'})
    
    # Get initial state of todos
    rv = client.get('/')
    assert b'Delete test' in rv.data
    assert b'Another task' in rv.data

    # Then delete the first one
    rv = client.get('/delete/0')
    assert rv.status_code == 302  # Redirect
    
    # Verify the first task is gone
    rv = client.get('/')
    assert b'Delete test' not in rv.data  # Should be removed
    assert b'Another task' in rv.data  # Ensure other task is still present