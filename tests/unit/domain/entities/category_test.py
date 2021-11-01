import uuid

import pytest

from src.domain.entities import Category


def test_category_model_init():
    id = uuid.uuid4()
    category = Category(id, name="Categoria 1", description="Descrição da categoria 1")

    assert category.id == id
    assert category.name == "Categoria 1"
    assert category.description == "Descrição da categoria 1"


def test_category_model_post_init():
    id = uuid.uuid4()
    with pytest.raises(TypeError):
        Category(id, description="Descrição da categoria 1")


def test_category_model_from_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "name": "Categoria 1",
        "description": "Descrição da categoria 1",
    }

    category = Category.from_dict(init_dict)

    assert category.id == id
    assert category.name == "Categoria 1"
    assert category.description == "Descrição da categoria 1"


def test_category_model_to_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "name": "Categoria 1",
        "description": "Descrição da categoria 1",
        "is_active": True,
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    }

    category = Category.from_dict(init_dict)

    assert category.to_dict() == init_dict


def test_category_model_comparison():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "name": "Categoria 1",
        "description": "Descrição da categoria 1",
        "is_active": True,
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    }

    category1 = Category.from_dict(init_dict)
    category2 = Category.from_dict(init_dict)

    assert category1 == category2
