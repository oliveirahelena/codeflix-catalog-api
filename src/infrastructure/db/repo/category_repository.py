import uuid
from typing import Set, Union

from sqlalchemy.orm import Session

from src.domain.entities import Category, Genre, Video
from src.infrastructure.db.models import orm

from .repository import SQLAlquemyRepository


class CategoryRepository(SQLAlquemyRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.model = Category

    @classmethod
    def get_by_genre(cls, genre_id: uuid.UUID) -> Union[Set[Category], None]:
        return (
            cls.session.query(Category)
            .join(Genre)
            .filter(
                orm.genres.c.id == genre_id,
            )
        )

    @classmethod
    def get_by_video(cls, video_id: uuid.UUID) -> Union[Set[Category], None]:
        return (
            cls.session.query(Category)
            .join(Video)
            .filter(
                orm.videos.c.id == video_id,
            )
        )
