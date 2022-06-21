from domain.repository.ArtObjectRepository import ArtObjectRepository


class GetArtObjectsUseCase:
    def __init__(self, artObjectRepository: ArtObjectRepository):
        self.artObjectRepository = artObjectRepository

    def execute(self, ArtObjectHeadlinesQuery):
        return self.artObjectRepository.get_art_objects(ArtObjectHeadlinesQuery)
