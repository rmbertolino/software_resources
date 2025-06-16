from abc import ABC, abstractmethod

from resources.domain.models import Resource

class ResourceRepository(ABC):
    @abstractmethod
    def get(self) -> Resource: ...