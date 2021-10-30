import uuid
from abc import ABCMeta, abstractmethod
from typing import Set, Union

from src.domain.entities.entity import Entity


class RepositoryInterface(metaclass=ABCMeta):
    """An interface for a generic repository with CRUD operations"""

    @abstractmethod
    @classmethod
    def list(self, **kwargs) -> Union[Set[Entity], None]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: uuid.UUID) -> Union[Entity, None]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, entity: Entity) -> Union[Entity, None]:
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: Entity) -> Union[Entity, None]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity_id: uuid.UUID) -> bool:
        raise NotImplementedError

    @staticmethod
    def next_id() -> uuid.UUID:
        return uuid.uuid4()
