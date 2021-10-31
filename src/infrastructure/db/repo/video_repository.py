import uuid
from typing import Set, Union

from sqlalchemy.orm import Session

from src.domain.entities import CastMember, Category, Genre, Video
from src.infrastructure.db.models import orm

from .repository import SQLAlquemyRepository


class VideoRepository(SQLAlquemyRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.model = Video

    @classmethod
    def get_by_category(cls, category_id: uuid.UUID) -> Union[Set[Video], None]:
        return (
            cls.session.query(Video)
            .join(Category)
            .filter(
                orm.categories.c.id == category_id,
            )
        )

    @classmethod
    def get_by_genre(cls, genre_id: uuid.UUID) -> Union[Set[Video], None]:
        return (
            cls.session.query(Video)
            .join(Genre)
            .filter(
                orm.genres.c.id == genre_id,
            )
        )

    @classmethod
    def get_by_cast_member(cls, cast_member_id: uuid.UUID) -> Union[Set[Video], None]:
        return (
            cls.session.query(Video)
            .join(CastMember)
            .filter(
                orm.cast_members.c.id == cast_member_id,
            )
        )
