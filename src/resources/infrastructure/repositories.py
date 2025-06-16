from resources.domain.models import Resource
from resources.domain.repositories import ResourceRepository


class PostgreSQLResourceRepository(ResourceRepository):
    def get(self) -> Resource:
        return Resource()