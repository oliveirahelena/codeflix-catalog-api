from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        "sqlite:///storage.db",
        isolation_level="REPEATABLE READ",
    )
)
