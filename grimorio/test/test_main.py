"""TEST"""

import random
import string

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_register():
    test_id = ''.join(random.choices(string.ascii_lowercase +string.digits, k=10))
    send_json = {
        "name": "TestUser",
        "lastname": "TestLastName",
        "magical_affinity": "Agua",
        "identidication": test_id,
        "age": 18
    }
    response = client.post(
        "/solicitud",
        json=send_json,
    )
    assert response.status_code == 200

def test_update():
    test_id = ''.join(random.choices(string.ascii_lowercase +string.digits, k=10))
    send_json = {
        "name": "Updated",
        "lastname": "Change",
        "magical_affinity": "Agua",
        "identidication": test_id,
        "age": 18
    }
    response = client.post(
        "/solicitud",
        json=send_json,
    )
    user_id = response.json()["student"]["id"]
    send_json = {
        "name": "Updated2",
        "lastname": "Change2",
        "magical_affinity": "Fuego",
        "identidication": test_id,
        "age": 18
    }
    response = client.put(
        f"/solicitud/{user_id}",
        json=send_json,
    )
    print(response.json())
    assert response.status_code == 200
    json_response = {
        "message": "ok",
        "code": 200,
        "student": user_id
    }
    assert response.json() == json_response

def test_patch():
    test_id = ''.join(random.choices(string.ascii_lowercase +string.digits, k=10))
    send_json = {
        "name": "Patch",
        "lastname": "user",
        "magical_affinity": "Agua",
        "identidication": test_id,
        "age": 18
    }
    response = client.post(
        "/solicitud",
        json=send_json,
    )
    user_id = response.json()["student"]["id"]
    print(user_id)
    send_json = {
        "approved": True
    }
    response = client.patch(
        f"/solicitud/{user_id}/status",
        json=send_json
    )
    print(response.json())
    assert response.status_code == 200

def test_delete():
    test_id = ''.join(random.choices(string.ascii_lowercase +string.digits, k=10))
    send_json = {
        "name": "Deleted",
        "lastname": "Change",
        "magical_affinity": "Agua",
        "identidication": test_id,
        "age": 18
    }
    response = client.post(
        "/solicitud",
        json=send_json,
    )
    user_id = response.json()["student"]["id"]
    send_json = {
        "name": "Updated2",
        "lastname": "Change2",
        "magical_affinity": "Fuego",
        "identidication": test_id,
        "age": 18
    }
    response = client.delete(
        f"/solicitud/{user_id}"
    )
    print(response.json())
    assert response.status_code == 200
    json_response = {
        "message": "deleted",
        "code": 200,
        "student": user_id
    }
    assert response.json() == json_response

def test_get_students():
    response = client.get("/solicitudes")
    assert response.status_code == 200

def test_get_grimorios():
    response = client.get("/asignaciones")
    assert response.status_code == 200
