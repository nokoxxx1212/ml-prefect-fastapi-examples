from fastapi.testclient import TestClient
from src.presentation.main import app

client = TestClient(app)

def test_get_recommendations():
    response = client.get("/recommendations?user_id=test_user")
    assert response.status_code == 200
    assert response.json() == {"recommendations": ["item1", "item2", "item3"]}
