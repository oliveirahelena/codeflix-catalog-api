import uuid
from typing import Set, Type, Union

from sqlalchemy.orm import Session

from src.data.interfaces import RepositoryInterface
from src.domain.entities import Entity


class SQLAlquemyRepository(RepositoryInterface):
    model: Type[Entity]

    def __init__(self, session: Session):
        self.session = session

    @classmethod
    def list(cls, **kwargs) -> Union[Set[Entity], None]:
        return cls.session.query(cls.model).filter_by(**kwargs)

    def get_by_id(self, id: uuid.UUID) -> Union[Entity, None]:
        return self.session.query(self.model).filter_by(id=id).first()

    def insert(self, entity: Entity) -> Union[Entity, None]:
        return self.session.add(entity)

    def update(self, entity: Entity) -> Union[Entity, None]:
        return (
            self.session.query(self.model).filter(entity.id == entity.id).update(entity)
        )

    def delete(self, entity_id: uuid.UUID) -> bool:
        return (
            self.session.query(self.model)
            .filter(self.model.id == entity_id)
            .delete(synchronize_session=False)
        )

    @staticmethod
    def next_id() -> uuid.UUID:
        return uuid.uuid4()

    def count(self) -> int:
        return self.session.query(self.model).count()
