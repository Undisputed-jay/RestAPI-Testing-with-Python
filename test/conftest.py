import pytest
from utilities.configurations import get_config
from utilities.resources import ApiResources
import requests
import json
from payload import createUserPayload, updateUser

@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}

@pytest.fixture
def base_url():
    return get_config()["API"]["baseurl"]

@pytest.fixture
def make_request(headers):
    def _make_request(method, url, payload=None):
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=payload, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=payload, headers=headers)
        elif method == "PATCH":
            response = requests.patch(url, json=payload, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        return response

    return _make_request
