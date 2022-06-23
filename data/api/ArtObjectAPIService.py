import json
from typing import List

import requests
from domain.model.APIResponse import APIResponsefromdict, APIResponse, ArtObject


class ArtObjectAPIService:
    @staticmethod
    def get_art_objects(query) -> List[ArtObject]:
        url = query.base_url + "/api/" + query.language + "/collection?key=" + query.api_key
        params = {'ps': query.page_size, 'p': str(query.page)}
        response = requests.get(url, params)
        return APIResponsefromdict(json.loads(response.text)).artObjects
