import logging

from sqlalchemy import Column, MetaData, String, Table
from sqlalchemy.orm import mapper

from src.domain.entities import Entity

logger = logging.getLogger(__name__)

metadata = MetaData()

demo_table = Table(
    "demo_table",
    metadata,
    Column("id", String(255), primary_key=True),
)


def start_mappers():
    """Starting mappers"""

    logger.info("Starting mappers")
    mapper(Entity, demo_table)
