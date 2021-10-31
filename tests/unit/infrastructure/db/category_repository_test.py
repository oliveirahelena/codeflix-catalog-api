import uuid

import pytest

from src.domain.entities import Category
from src.infrastructure.db.repo import CategoryRepository

pytestmark = pytest.mark.usefixtures("mappers")


def test_insert_category(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = CategoryRepository(session)

    id = uuid.uuid4()
    category = Category(id=id, name="Categoria1", description="Descrição da Categoria")

    repo.insert(category)

    assert repo.get_by_id(id) == category
