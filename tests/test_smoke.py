import os

os.environ["MOCK_AI"] = "true"

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    assert "ComicCraft" in response.text


def test_json_generation():
    payload = {
        "story_prompt": "A fox discovers a secret door.",
        "character_name": "Milo",
        "setting": "Enchanted Forest",
        "tone": "Funny",
        "art_style": "Comic Book"
    }

    response = client.post(
        "/generate-comic/json",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["panels"]) == 5

    assert data["pdf_url"].endswith(".pdf")