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

# def generate_property_id(publisher_id):
#     now = date.now()
#     internals = publisher_id + now.isoformat()
#     return uuid4(internals)

def generate_property_id():
    return str(uuid4())

class Property(BaseModel):
    # Field() generates dynamically a new value
    # property_id: UUID = Field(default_factory=generate_property_id)
    property_id: str = Field(default_factory=generate_property_id)
    crawl_date: date = Field(default_factory=date.today)
    realestatesite: RealEstateSite
    # publisher_id: UUID
    # property_features: Dict[str, Any] # property_id will be generated and pass by the crawler 
    title: str
    # Optional is used for fields that not always will be present
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




# Usage 

property_1 = Property(
    realestatesite=RealEstateSite.Lamudi,
    title="Beautiful Apartment in Downtown",
    json_script={"example": "data"},
    price=250000.0,
    community_fees=150.0,
    building_area=120.0,
    surface_area=150.0,
    publication_date=date(2023, 11, 12),
    images_urls=["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
    publisher_name="John Doe",
    publisher_phone="123-456-7890",
    publisher_url="https://example.com/profile",
    condition="New",
    construction_year=2020,
    secondary_json={"info": "details"},
    secondary_description="Great location, modern design",
    facilities=["pool", "gym", "parking"],
    nearby_locations=["park", "mall"],
    item_url="https://example.com/property/123",
    state="New York",
    kind="Apartment",
)

# print(property_1)

property_2_dict = {
    "realestatesite": "lmd",
    "title": "Beautiful Apartment in Downtown",
    "json_script": {"example": "data"},
    "price": 250000.0,
    "community_fees": 150.0,
    "building_area": 120.0,
    "surface_area": 150.0,
    "publication_date": "2023-11-12",
    "images_urls": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
    "publisher_name": "John Doe",
    "publisher_phone": "000000000000",
    "publisher_url": "https://example.com/profile",
    "condition": "New",
    "construction_year": 2020,
    "secondary_json": {"info": "details"},
    "secondary_description": "Great location, modern design",
    "facilities": ["pool", "gym", "parking"],
    "nearby_locations": ["park", "mall"],
    "item_url": "https://example.com/property/123",
    "state": "New York",
    "kind": "Apartment",
}

property_2 = Property.model_validate(property_2_dict)

print(property_2)