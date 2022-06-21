from dataclasses import dataclass


@dataclass
class ArtObjectHeadlinesQuery:
    language: str
    page_size: int
    page: int
    base_url: str = "https://www.rijksmuseum.nl"
    api_key: str = "wiqcGm4R"
