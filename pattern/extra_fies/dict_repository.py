from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from pattern.extra_fies.pydantic_models import RealEstateSite, Property
from datetime import date
import pdb

class PropertyRepository(ABC):
    @abstractmethod
    def get_property(self, id: int) -> property:
        pass

    @abstractmethod
    def create_property(self, property: property) -> property:
        pass

    @abstractmethod
    def update_property(self, property: property) -> property:
        pass

    @abstractmethod
    def delete_property(self, id: int) -> None:
        pass

################
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

####################

properties_dict = {}

class LocalDictRepository(PropertyRepository):
    
    def get_property(self, property_id: str) -> Optional[Property]:
        if property_id not in properties_dict:
            print(f"{property_id} does not exist.")
            return None
        return properties_dict[property_id]
    
    def create_property(self, property: Property) -> Optional[Property]:
        if property.property_id in properties_dict:
            print(f"{property.property_id} already exists.")
            return None
        properties_dict[property.property_id] = property
        # print(properties_dict[property.property_id])
        return properties_dict[property.property_id]

    def update_property(self, property: Property) -> None:
        if property.property_id not in properties_dict:
            print(f"{property.property_id} does not exist.")
            return None
        properties_dict[property.property_id] = property
        return properties_dict[property.property_id]

    def delete_property(self, property_id: int) -> None:
        if property_id not in properties_dict:
            print(f"{property_id} does not exist.")
            return None
        properties_dict.pop(property_id)



repo = LocalDictRepository()
pdb.set_trace()

repo.create_property(property_1)

