from domain.model.APIResponse import APIResponse


class ArtObjectRepositoryImpl:
    def __init__(self, ArtObjectAPIService):
        self.ArtObjectAPIService = ArtObjectAPIService
        self.artObjects = []

    def get_art_objects(self, ArtObjectHeadlinesQuery) -> APIResponse:
        return self.ArtObjectAPIService.get_art_objects(ArtObjectHeadlinesQuery)
