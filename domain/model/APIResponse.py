from dataclasses import dataclass
from uuid import UUID
from typing import Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Image:
    guid: UUID
    offsetPercentageX: int
    offsetPercentageY: int
    width: int
    height: int
    url: str

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        guid = UUID(obj.get("guid"))
        offsetPercentageX = from_int(obj.get("offsetPercentageX"))
        offsetPercentageY = from_int(obj.get("offsetPercentageY"))
        width = from_int(obj.get("width"))
        height = from_int(obj.get("height"))
        url = from_str(obj.get("url"))
        return Image(guid, offsetPercentageX, offsetPercentageY, width, height, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["guid"] = str(self.guid)
        result["offsetPercentageX"] = from_int(self.offsetPercentageX)
        result["offsetPercentageY"] = from_int(self.offsetPercentageY)
        result["width"] = from_int(self.width)
        result["height"] = from_int(self.height)
        result["url"] = from_str(self.url)
        return result


@dataclass
class Links:
    linksself: str
    web: str

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        assert isinstance(obj, dict)
        linksself = from_str(obj.get("self"))
        web = from_str(obj.get("web"))
        return Links(linksself, web)

    def to_dict(self) -> dict:
        result: dict = {}
        result["self"] = from_str(self.linksself)
        result["web"] = from_str(self.web)
        return result


@dataclass
class ArtObject:
    links: Links
    id: str
    objectNumber: str
    title: str
    hasImage: bool
    principalOrFirstMaker: str
    longTitle: str
    showImage: bool
    permitDownload: bool
    webImage: Image
    headerImage: Image
    productionPlaces: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'ArtObject':
        assert isinstance(obj, dict)
        links = Links.from_dict(obj.get("links"))
        id = from_str(obj.get("id"))
        objectNumber = from_str(obj.get("objectNumber"))
        title = from_str(obj.get("title"))
        hasImage = from_bool(obj.get("hasImage"))
        principalOrFirstMaker = from_str(obj.get("principalOrFirstMaker"))
        longTitle = from_str(obj.get("longTitle"))
        showImage = from_bool(obj.get("showImage"))
        permitDownload = from_bool(obj.get("permitDownload"))
        webImage = Image.from_dict(obj.get("webImage"))
        headerImage = Image.from_dict(obj.get("headerImage"))
        productionPlaces = from_list(from_str, obj.get("productionPlaces"))
        return ArtObject(links, id, objectNumber, title, hasImage, principalOrFirstMaker, longTitle, showImage,
                         permitDownload, webImage, headerImage, productionPlaces)

    def to_dict(self) -> dict:
        result: dict = {}
        result["links"] = to_class(Links, self.links)
        result["id"] = from_str(self.id)
        result["objectNumber"] = from_str(self.objectNumber)
        result["title"] = from_str(self.title)
        result["hasImage"] = from_bool(self.hasImage)
        result["principalOrFirstMaker"] = from_str(self.principalOrFirstMaker)
        result["longTitle"] = from_str(self.longTitle)
        result["showImage"] = from_bool(self.showImage)
        result["permitDownload"] = from_bool(self.permitDownload)
        result["webImage"] = to_class(Image, self.webImage)
        result["headerImage"] = to_class(Image, self.headerImage)
        result["productionPlaces"] = from_list(from_str, self.productionPlaces)
        return result


@dataclass
class CountFacets:
    hasimage: int
    ondisplay: int

    @staticmethod
    def from_dict(obj: Any) -> 'CountFacets':
        assert isinstance(obj, dict)
        hasimage = from_int(obj.get("hasimage"))
        ondisplay = from_int(obj.get("ondisplay"))
        return CountFacets(hasimage, ondisplay)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hasimage"] = from_int(self.hasimage)
        result["ondisplay"] = from_int(self.ondisplay)
        return result


@dataclass
class FacetFacet:
    key: str
    value: int

    @staticmethod
    def from_dict(obj: Any) -> 'FacetFacet':
        assert isinstance(obj, dict)
        key = from_str(obj.get("key"))
        value = from_int(obj.get("value"))
        return FacetFacet(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_str(self.key)
        result["value"] = from_int(self.value)
        return result


@dataclass
class APIResponseFacet:
    facets: List[FacetFacet]
    name: str
    otherTerms: int
    prettyName: int

    @staticmethod
    def from_dict(obj: Any) -> 'APIResponseFacet':
        assert isinstance(obj, dict)
        facets = from_list(FacetFacet.from_dict, obj.get("facets"))
        name = from_str(obj.get("name"))
        otherTerms = from_int(obj.get("otherTerms"))
        prettyName = from_int(obj.get("prettyName"))
        return APIResponseFacet(facets, name, otherTerms, prettyName)

    def to_dict(self) -> dict:
        result: dict = {}
        result["facets"] = from_list(lambda x: to_class(FacetFacet, x), self.facets)
        result["name"] = from_str(self.name)
        result["otherTerms"] = from_int(self.otherTerms)
        result["prettyName"] = from_int(self.prettyName)
        return result


@dataclass
class APIResponse:
    elapsedMilliseconds: int
    count: int
    countFacets: CountFacets
    artObjects: List[ArtObject]
    facets: List[APIResponseFacet]

    @staticmethod
    def from_dict(obj: Any) -> 'APIResponse':
        assert isinstance(obj, dict)
        elapsedMilliseconds = from_int(obj.get("elapsedMilliseconds"))
        count = from_int(obj.get("count"))
        countFacets = CountFacets.from_dict(obj.get("countFacets"))
        artObjects = from_list(ArtObject.from_dict, obj.get("artObjects"))
        facets = from_list(APIResponseFacet.from_dict, obj.get("facets"))
        return APIResponse(elapsedMilliseconds, count, countFacets, artObjects, facets)

    def to_dict(self) -> dict:
        result: dict = {}
        result["elapsedMilliseconds"] = from_int(self.elapsedMilliseconds)
        result["count"] = from_int(self.count)
        result["countFacets"] = to_class(CountFacets, self.countFacets)
        result["artObjects"] = from_list(lambda x: to_class(ArtObject, x), self.artObjects)
        result["facets"] = from_list(lambda x: to_class(APIResponseFacet, x), self.facets)
        return result


def APIResponsefromdict(s: Any) -> APIResponse:
    return APIResponse.from_dict(s)
