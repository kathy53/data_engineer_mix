from typing import Optional
from app.models.property import Property
from app.repositories.base_repository import PropertyRepository

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