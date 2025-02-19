from dataclasses import dataclass, field

@dataclass
class DataModel:
    name: str = field(default="")
    type: str = field(default="")
    price: str = field(default="")
    size: str = field(default="")
    url_img: str = field(default="")
    place: str = field(default="")
    poster: str = field(default="")
    url: str = field(default="")