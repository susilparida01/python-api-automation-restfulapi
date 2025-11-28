import requests
from typing import Any,Dict,Optional, List
from config.settings import BASE_URL,OBJECTS_ENDPOINTS

class RestfulApiClient:
    """ Client wrapper for https://restful-api.dev """

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url.rstrip("/")

    def _url(self,path: str) -> str:
        return f"{self.base_url}{path}"

    # -------- GET METHODS ------------------------
    def get_all_objects(self) -> requests.Response:
        return requests.get(self._url(OBJECTS_ENDPOINTS))

    def get_object(self, object_id: str | int) -> requests.Response:
        return requests.get(self._url(f"{OBJECTS_ENDPOINTS}/{object_id}"))

    def get_objects_ids(self,ids: List[str | int]) -> requests.Response:
        ids_param = ",".join(str(i) for i in ids)
        return requests.get(self._url(OBJECTS_ENDPOINTS), params={"id": ids_param})


    # -------- CREATE/UPDATE/DELETE -----------------
    def create_object(self,name: str, data: Optional[Dict[str, Any]] = None) -> requests.Response:
        payload: Dict[str, Any] = {"name": name}
        if data is not None:
            payload["data"] = data
        return requests.post(self._url(OBJECTS_ENDPOINTS), json=payload)

    def update_object_put(self,object_id: str | int, name: str, data: Dict[str,Any]) -> requests.Response:
        payload = {"name": name, "data": data}
        return requests.put(self._url(f"{OBJECTS_ENDPOINTS}/{object_id}"), json=payload)

    def delete_object(self, object_id: str | int) -> requests.Response:
        return requests.delete(self._url(f"{OBJECTS_ENDPOINTS}/{object_id}"))
