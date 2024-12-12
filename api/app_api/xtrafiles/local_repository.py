from typing import Optional, Dict
from app_api.xtrafiles.property import Property
from app_api.xtrafiles.base_repository import PropertyRepository

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

    def delete_property(self, property_id: str) -> None:
        if property_id not in properties_dict:
            print(f"{property_id} does not exist.")
            return None
        properties_dict.pop(property_id)
        return None

    def get_reduced_property(self, property_id: str) -> Optional[Dict[str, str]]:
        if property_id not in properties_dict:
            print(f"{property_id} does not exist.")
            return None
        reduced_property = {key:value for key, value in properties_dict[property_id] if key in ["property_id", "crawl_date", "realestatesite"]}
        return reduced_property