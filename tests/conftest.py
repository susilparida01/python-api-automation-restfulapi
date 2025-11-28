import pytest
from src.api_client import RestfulApiClient

@pytest.fixture(scope="session")
def api_client() -> RestfulApiClient:
    """ Shared API client instance for all tests"""
    return RestfulApiClient()

def new_object(api_client: RestfulApiClient):
    """
    Creates a new object before the test and deleted it after the test.
    Demonstrates setup & teardown with yield fixture.
    """
    create_resp = api_client.create_object(
        name = "Apple MacBook Pro 16",
        data = {"year": 2025,
                "price": 11849.99,
                "CPU model": "Intel Core i12",
                "Hard disk size": "2 TB"}
    )
    assert create_resp.status_code == 200 or create_resp.status_code == 201
    body = create_resp.json()
    obj_id = body.get("id")
    assert obj_id is not None

    # Provide object details to the test
    yield body

    # Teardown: delete the created object
    if obj_id is not None:
        api_client.delete_object(obj_id)