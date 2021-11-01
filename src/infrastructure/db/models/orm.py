import logging
from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, Enum, Float, ForeignKey,
                        Integer, MetaData, String, Table)
from sqlalchemy.orm import mapper, relationship

from src.domain.entities import (CastMember, CastMemberTypes, Category, Genre,
                                 Video)
from src.infrastructure.db.utils import GUID

logger = logging.getLogger(__name__)

metadata = MetaData()

category_genre = Table(
    "category_genre",
    metadata,
    Column("category_id", GUID(), ForeignKey("categories.id"), primary_key=True),
    Column("genre_id", GUID(), ForeignKey("genres.id"), primary_key=True),
)

genre_video = Table(
    "genre_video",
    metadata,
    Column("genre_id", GUID(), ForeignKey("genres.id"), primary_key=True),
    Column("video_id", GUID(), ForeignKey("videos.id"), primary_key=True),
)

category_video = Table(
    "category_video",
    metadata,
    Column("category_id", GUID(), ForeignKey("categories.id"), primary_key=True),
    Column("video_id", GUID(), ForeignKey("videos.id"), primary_key=True),
)

cast_member_video = Table(
    "cast_member_video",
    metadata,
    Column(
        "cast_members_id",
        GUID(),
        ForeignKey("cast_members.id"),
        primary_key=True,
    ),
    Column("video_id", GUID(), ForeignKey("videos.id"), primary_key=True),
)

videos = Table(
    "videos",
    metadata,
    Column("id", GUID(), primary_key=True),
    Column("title", String(255)),
    Column("description", String()),
    Column("year_launched", Integer()),
    Column("opened", Boolean()),
    Column("rating", String(10)),
    Column("duration", Float()),
    Column("thumb_file", String(255)),
    Column("banner_file", String(255)),
    Column("trailer_file", String(255)),
    Column("video_file", String(255)),
    Column("deleted_at", DateTime(), nullable=True),
    Column("updated_at", DateTime(), onupdate=datetime.utcnow),
    Column("created_at", DateTime(), default=datetime.utcnow),
)

cast_members = Table(
    "cast_members",
    metadata,
    Column("id", GUID(), primary_key=True),
    Column("name", String(255)),
    Column("type", Enum(CastMemberTypes), nullable=False),
    Column("deleted_at", DateTime(), nullable=True),
    Column("updated_at", DateTime(), onupdate=datetime.utcnow),
    Column("created_at", DateTime(), default=datetime.utcnow),
)

categories = Table(
    "categories",
    metadata,
    Column("id", GUID(), primary_key=True),
    Column("name", String(255)),
    Column("description", String()),
    Column("is_active", Boolean()),
    Column("deleted_at", DateTime(), nullable=True),
    Column("updated_at", DateTime(), onupdate=datetime.utcnow),
    Column("created_at", DateTime(), default=datetime.utcnow),
)

genres = Table(
    "genres",
    metadata,
    Column("id", GUID(), primary_key=True),
    Column("name", String(255)),
    Column("is_active", Boolean()),
    Column("deleted_at", DateTime(), nullable=True),
    Column("updated_at", DateTime(), onupdate=datetime.utcnow),
    Column("created_at", DateTime(), default=datetime.utcnow),
)


def start_mappers():
    """Starting mappers"""

    logger.info("Starting mappers")
    mapper(
        Genre,
        genres,
        properties={
            "categories": relationship(
                Category,
                secondary=category_genre,
                back_populates="genres",
                collection_class=set,
            ),
            "videos": relationship(
                Video,
                secondary=genre_video,
                back_populates="genres",
                collection_class=set,
            ),
        },
    )
    mapper(
        Category,
        categories,
        properties={
            "genres": relationship(
                Genre,
                secondary=category_genre,
                back_populates="categories",
                collection_class=set,
            ),
            "videos": relationship(
                Video,
                secondary=category_video,
                back_populates="categories",
                collection_class=set,
            ),
        },
    )
    mapper(
        Video,
        videos,
        properties={
            "genres": relationship(
                Genre,
                secondary=genre_video,
                back_populates="videos",
                collection_class=set,
            ),
            "categories": relationship(
                Category,
                secondary=category_video,
                back_populates="videos",
                collection_class=set,
            ),
            "cast_members": relationship(
                CastMember,
                secondary=cast_member_video,
                back_populates="videos",
                collection_class=set,
            ),
        },
    )
    mapper(
        CastMember,
        cast_members,
        properties={
            "videos": relationship(
                Video,
                secondary=cast_member_video,
                back_populates="cast_members",
                collection_class=set,
            ),
        },
    )
