import uuid
from typing import Set, Union

from sqlalchemy.orm import Session

from src.domain.entities import CastMember, Video
from src.infrastructure.db.models import orm

from .repository import SQLAlquemyRepository


class CastMemberRepository(SQLAlquemyRepository):
    def __init__(self, session: Session):
        super().__init__(session)
        self.model = CastMember

    @classmethod
    def get_by_video(cls, video_id: uuid.UUID) -> Union[Set[CastMember], None]:
        return (
            cls.session.query(CastMember)
            .join(Video)
            .filter(
                orm.videos.c.id == video_id,
            )
        )
