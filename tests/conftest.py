# pylint: disable=redefined-outer-name
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers, sessionmaker

from src.infrastructure.db.models import metadata, start_mappers


@pytest.fixture
def in_memory_sqlite_db():
    """Create in memory sqlite engine for tests"""

    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def sqlite_session_factory(in_memory_sqlite_db):
    """Create a session with sqlite engine for tests"""

    yield sessionmaker(bind=in_memory_sqlite_db)


@pytest.fixture
def mappers():
    """Cria as tabelas no Banco de dados"""
    start_mappers()
    yield
    clear_mappers()
