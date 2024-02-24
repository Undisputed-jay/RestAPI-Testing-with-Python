import pytest
from conftest import *
from utilities.resources import ApiResources
from payload import *

def test_list_users(base_url, headers, make_request):
    url = base_url + ApiResources.list_users
    response = make_request("GET", url)
    assert response.status_code == 200

def test_get_single_user(base_url, headers, make_request):
    url = base_url + ApiResources.get_single_users
    response = make_request("GET", url)
    assert response.status_code == 200
    jsonData = response.json()
    assert jsonData['data']['first_name'] == "Janet"

def test_single_user_not_found(base_url, headers, make_request):
    url = base_url + ApiResources.user_not_found
    response = make_request("GET", url)
    assert response.status_code == 404

def test_list_resource(base_url, headers, make_request):
    url = base_url + ApiResources.list_resource
    response = make_request("GET", url)
    assert response.status_code == 200
    jsonData = response.json()
    assert jsonData['data'][2]['color'] == "#BF1932"

def test_list_single_resource(base_url, headers, make_request):
    url = base_url + ApiResources.list_single_resource
    response = make_request("GET", url)
    assert response.status_code == 200
    jsonData = response.json()
    assert jsonData['data']['name'] == "fuchsia rose"

def test_single_resource_not_found(base_url, headers, make_request):
    url = base_url + ApiResources.resource_not_found
    response = make_request("GET", url)
    assert response.status_code == 404

def test_create_user(base_url, headers, make_request):
    url = base_url + ApiResources.create_user
    payload = createUserPayload()
    response = make_request("POST", url, payload=payload)
    assert response.status_code == 201

def test_update_user(base_url, headers, make_request):
    url = base_url + ApiResources.get_single_users
    payload = updateUser()
    response = make_request("PUT", url, payload=payload)
    assert response.status_code == 200

def test_edit_user(base_url, headers, make_request):
    url = base_url + ApiResources.get_single_users
    payload = updateUser()
    response = make_request("PATCH", url, payload=payload)
    assert response.status_code == 200

def test_delete_user(base_url, headers, make_request):
    url = base_url + ApiResources.get_single_users
    response = make_request("DELETE", url)
    assert response.status_code == 204

def test_register(base_url, headers, make_request):
    url = base_url + ApiResources.register
    payload = registerUser()
    response = make_request("POST", url, payload=payload)
    assert response.status_code == 200
    jsonData = response.json()
    assert jsonData['id'] == 4

def test_wrong_register(base_url, headers, make_request):
    url = base_url + ApiResources.register
    payload = registerUserIncomplete()
    response = make_request("POST", url, payload=payload)
    assert response.status_code == 400
    jsonData = response.json()
    assert jsonData['error'] == "Missing password"

def test_login(base_url, headers, make_request):
    url = base_url + ApiResources.login
    payload = loginUser()
    response = make_request("POST", url, payload=payload)
    assert response.status_code == 200

def test_wrong_login(base_url, headers, make_request):
    url = base_url + ApiResources.login
    payload = loginWrongUser()
    response = make_request("POST", url, payload=payload)
    assert response.status_code == 400

def test_delayed_response(base_url, headers, make_request):
    url = base_url + ApiResources.delayed_response
    response = make_request("GET", url)
    assert response.status_code == 200
    jsonData = response.json()
    assert jsonData['data'][3]['last_name'] == 'Holt'
