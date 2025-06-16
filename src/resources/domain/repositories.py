from abc import ABC, abstractmethod

from resources.domain.models import Resource

class ResourceRepository(ABC):
    @abstractmethod
    def all(self) -> list[Resource]: ...

    @abstractmethod
    def save(self, resource: Resource) -> None: ...