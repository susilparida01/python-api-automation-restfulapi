import pytest

def test_get_all_objects_status_and_structure(api_client):
    resp = api_client.get_all_objects()
    assert resp.status_code == 200

    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0

@pytest.mark.parametrize("object_id", ["5"])
def test_get_single_object_by_id(api_client,object_id):
    resp = api_client.get_object(object_id)
    assert resp.status_code == 200

    body = resp.json()
    assert str(body["id"]) == str(object_id)




