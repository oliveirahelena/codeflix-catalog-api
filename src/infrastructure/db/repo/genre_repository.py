import uuid
from typing import Set, Union

from sqlalchemy.orm import Session

from src.domain.entities import Category, Genre, Video
from src.infrastructure.db.models import orm

from .repository import SQLAlquemyRepository


class GenreRepository(SQLAlquemyRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.model = Genre

    @classmethod
    def get_by_category(cls, category_id: uuid.UUID) -> Union[Set[Genre], None]:
        return (
            cls.session.query(Genre)
            .join(Category)
            .filter(
                orm.categories.c.id == category_id,
            )
        )

    @classmethod
    def get_by_video(cls, video_id: uuid.UUID) -> Union[Set[Genre], None]:
        return (
            cls.session.query(Genre)
            .join(Video)
            .filter(
                orm.videos.c.id == video_id,
            )
        )
