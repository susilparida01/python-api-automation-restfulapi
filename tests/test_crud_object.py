import pytest

def test_full_crud_flow(api_client):
    # ----- CREATE ------
    create_resp = api_client.create_object(
        name = "Apple MacBook Pro 16",
        data = {"year": 2025,
                "price": 11849.99,
                "CPU model": "Intel Core i12",
                "Hard disk size": "2 TB"
        }
    )

    assert create_resp.status_code in (200, 201)
    created = create_resp.json()
    obj_id = created.get("id")
    assert obj_id is not None

    # ----- READ (GET) ------
    get_resp = api_client.get_object(obj_id)
    assert get_resp.status_code == 200
    fetched = get_resp.json()
    assert fetched["name"] == "Apple MacBook Pro 16"

    # --- UPDATE(PUT) ---
    updated_price = 15000.00
    put_resp = api_client.update_object_put(
        obj_id,
        name="Apple MacBook Pro 18",
        data={"year": 2025,
              "price": updated_price,
              "CPU model": "Intel Core i12",
              "Hard disk size": "2 TB"
              }
    )

    assert put_resp.status_code == 200
    put_body = put_resp.json()
    assert put_body["name"] == "Apple MacBook Pro 18"
    assert put_body["data"]["price"] == updated_price

    # --- DELETE -----
    delete_resp = api_client.delete_object(obj_id)
    assert delete_resp.status_code in (200, 204)

    # --- VERIFY DELETED (should be 404 status code)
    get_after_deleted = api_client.get_object(obj_id)
    assert get_after_deleted.status_code == 404


