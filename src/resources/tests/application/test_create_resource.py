import pytest
from resources.application.create_resource import CreateResource, CreateResourceCommand
from resources.domain.exceptions import UrlIsNotValid
from resources.domain.models import Resource
from resources.domain.repositories import ResourceRepository
from resources.domain.value_objects import ResourceUrl

class FakeResourceRepository(ResourceRepository):
    def __init__(self):
        self._resources = []

    def save(self, resource: Resource) -> None:
        self._resources.append(resource)

    def all(self) -> list[Resource]:
        return list(self._resources)
    
class TestCreateResource:
    def test_create_resource(self) -> None:
        resource_repository = FakeResourceRepository()

        CreateResource(resource_repository).execute(
            CreateResourceCommand(resource_url="http://example.com/resource")
        )

        resources = resource_repository.all()
        assert len(resources) == 1
        assert resources[0].url() == ResourceUrl(value="http://example.com/resource") 
 
    def test_raise_exception_when_resource_url_is_not_a_valid_url(self) -> None:
        resource_repository = FakeResourceRepository()

        with pytest.raises(UrlIsNotValid):
            CreateResource(resource_repository).execute(
                CreateResourceCommand(resource_url="not_a_valid_url")
            )

        resources = resource_repository.all()
        assert len(resources) == 0