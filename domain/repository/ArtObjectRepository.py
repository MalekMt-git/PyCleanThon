from abc import ABCMeta, abstractmethod
from typing import List
from domain.model.APIResponse import ArtObject


class ArtObjectRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_art_objects(ArtObjectHeadlinesQuery) -> List[ArtObject]:
        raise NotImplementedError
