import uuid

import pytest

from src.domain.entities import Genre


def test_genre_model_init():
    id = uuid.uuid4()
    genre = Genre(id, name="Gênero 1")

    assert genre.id == id
    assert genre.name == "Gênero 1"


def test_genre_model_post_init():
    id = uuid.uuid4()
    with pytest.raises(TypeError):
        Genre(id)


def test_genre_model_from_dict():
    id = uuid.uuid4()
    init_dict = {"id": id, "name": "Gênero 1"}

    genre = Genre.from_dict(init_dict)

    assert genre.id == id
    assert genre.name == "Gênero 1"


def test_genre_model_to_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "name": "Gênero 1",
        "is_active": True,
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    }

    genre = Genre.from_dict(init_dict)

    assert genre.to_dict() == init_dict


def test_genre_model_comparison():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "name": "Gênero 1",
        "is_active": True,
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    }

    genre1 = Genre.from_dict(init_dict)
    genre2 = Genre.from_dict(init_dict)

    assert genre1 == genre2
