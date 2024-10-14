from fastapi.testclient import TestClient
from app.presentation.main import app

client = TestClient(app)

def test_get_recommendations():
    """
    /recommendationsエンドポイントのテスト。
    """
    response = client.get("/recommendations?user_id=test_user")
    assert response.status_code == 200
    assert response.json() == {"recommendations": ["item1", "item2", "item3"]}