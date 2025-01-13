# test_app.py
import pytest
from app import app  # Import your Flask app from app.py

# Use Flask's test client for testing routes
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the home route
def test_home(client):
    response = client.get('/')
    assert response.data == b"Welcome to the Advanced Flask App!"
    assert response.status_code == 200

# Test the /api/health route
def test_health_check(client):
    response = client.get('/api/health')
    assert response.json == {"status": "Healthy"}
    assert response.status_code == 200

# Test the /api/echo route with valid data
def test_echo(client):
    data = {"message": "Hello, World!"}
    response = client.post('/api/echo', json=data)
    assert response.json == {"echo": data}
    assert response.status_code == 200

# Test the /api/echo route with no data
def test_echo_no_data(client):
    response = client.post('/api/echo', json={})
    assert response.json == {"error": "No data provided"}
    assert response.status_code == 400
