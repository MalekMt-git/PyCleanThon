from typing import List

from domain.model.APIResponse import APIResponse, ArtObject


class ArtObjectRepositoryImpl:
    def __init__(self, ArtObjectAPIService):
        self.ArtObjectAPIService = ArtObjectAPIService
        self.artObjects = []

    def get_art_objects(self, ArtObjectHeadlinesQuery) -> List[ArtObject]:
        return self.ArtObjectAPIService.get_art_objects(ArtObjectHeadlinesQuery)
