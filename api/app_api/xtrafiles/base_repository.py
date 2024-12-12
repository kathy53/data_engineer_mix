from abc import ABC, abstractmethod
from app_api.xtrafiles.property import Property


class PropertyRepository(ABC):
    @abstractmethod
    def get_property(self, id: int) -> Property:
        pass

    @abstractmethod
    def create_property(self, property: Property) -> Property:
        pass

    @abstractmethod
    def update_property(self, property: Property) -> Property:
        pass

    @abstractmethod
    def delete_property(self, id: int) -> None:
        pass