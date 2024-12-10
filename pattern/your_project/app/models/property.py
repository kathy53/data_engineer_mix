from datetime import date
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional, Any, Dict

class RealEstateSite(Enum):
    Lamudi = "lmd"
    Trovit = "tr"
    I24 = "I24"
    Vivaanuncios = "van"


def generate_property_id():
    return str(uuid4())

class Property(BaseModel):
    property_id: str = Field(default_factory=generate_property_id)
    crawl_date: date = Field(default_factory=date.today)
    realestatesite: RealEstateSite
    title: str
    json_script: Optional[Any]
    price: float
    community_fees: Optional[float]
    building_area: Optional[float]
    surface_area: Optional[float]
    publication_date: Optional[date]
    images_urls: List[str]
    publisher_name: Optional[str]
    publisher_phone: Optional[str]
    publisher_url: Optional[str]
    condition: Optional[str]
    construction_year: Optional[int]
    secondary_json: Optional[Any]
    secondary_description: Optional[str]
    facilities: Optional[List[str]]
    nearby_locations: Optional[List[str]]
    item_url: str
    state: Optional[str]
    kind: Optional[str]

class Config:
   use_enum_values = True
