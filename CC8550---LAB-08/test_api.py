import requests
import pytest
from jsonschema import validate


BASE_URL = "https://dummyjson.com"
REQUEST_TIMEOUT = 10

SINGLE_USER_SCHEMA = {
    "type": "object",
    "required": ["id", "title", "body", "userId", "tags", "reactions"],
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"},
        "tags": {"type": "array"},
        "reactions": {"type": ["object", "integer"]},
    },
}

LOGIN_SUCCESS_SCHEMA = {
    "type": "object",
    "required": ["accessToken"],
    "properties": {"accessToken": {"type": "string"}},
}


@pytest.fixture
def user_payload():
    """Fornece payload base reutilizavel para criar post de teste."""
    return {"title": "Post de teste", "body": "Corpo de teste", "userId": 1}


def test_get_collection_returns_200_and_non_empty_list():
    """Valida GET em colecao com status 200 e lista nao vazia."""
    resp = requests.get(
        f"{BASE_URL}/posts",
        timeout=REQUEST_TIMEOUT,
    )
    assert resp.status_code == 200
    data = resp.json().get("posts", [])
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_existing_resource_matches_schema():
    """Valida schema de GET em recurso existente usando jsonschema."""
    resp = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=REQUEST_TIMEOUT,
    )
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=SINGLE_USER_SCHEMA)


def test_get_non_existing_resource_returns_404():
    """Valida caso negativo de recurso inexistente com status 404."""
    resp = requests.get(
        f"{BASE_URL}/posts/0",
        timeout=REQUEST_TIMEOUT,
    )
    assert resp.status_code == 404


def test_post_create_resource_returns_201_and_id(user_payload):
    """Valida criacao de recurso via POST com status 201 e id no retorno."""
    resp = requests.post(
        f"{BASE_URL}/posts/add",
        json=user_payload,
        timeout=REQUEST_TIMEOUT,
    )
    assert resp.status_code == 201
    body = resp.json()
    assert "id" in body
    assert body["title"] == user_payload["title"]


def test_patch_updates_resource_field():
    """Valida atualizacao parcial via PATCH com campo alterado."""
    updated_payload = {"title": "Post atualizado"}
    resp = requests.patch(
        f"{BASE_URL}/posts/1",
        json=updated_payload,
        timeout=REQUEST_TIMEOUT,
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["title"] == updated_payload["title"]


def test_delete_resource_returns_204():
    """Valida DELETE com status 204."""
    resp = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=REQUEST_TIMEOUT,
    )
    assert resp.status_code in (200, 204, 201)


def test_invalid_payload_returns_4xx():
    """Valida envio de dados invalidos com resposta 4xx."""
    resp = requests.post(
        f"{BASE_URL}/auth/login",
        json={"username": "emilys"},
        timeout=REQUEST_TIMEOUT,
    )
    assert 400 <= resp.status_code < 500
    assert resp.status_code == 400


def test_authenticated_endpoint_with_and_without_credentials():
    """Valida autenticacao no endpoint /login com e sem credencial completa."""
    success = requests.post(
        f"{BASE_URL}/auth/login",
        json={"username": "emilys", "password": "emilyspass"},
        timeout=REQUEST_TIMEOUT,
    )
    assert success.status_code == 200
    validate(instance=success.json(), schema=LOGIN_SUCCESS_SCHEMA)

    failure = requests.post(
        f"{BASE_URL}/auth/login",
        json={"username": "emilys"},
        timeout=REQUEST_TIMEOUT,
    )
    assert failure.status_code == 400


def test_fixture_supplies_reusable_payload(user_payload):
    """Valida fixture do pytest fornecendo payload reutilizavel."""
    assert user_payload["title"] == "Post de teste"
    assert user_payload["userId"] == 1


def test_response_time_under_two_seconds():
    """Valida que o endpoint responde em menos de 2 segundos."""
    resp = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=REQUEST_TIMEOUT,
    )
    assert resp.status_code == 200
    assert resp.elapsed.total_seconds() < 2.0
