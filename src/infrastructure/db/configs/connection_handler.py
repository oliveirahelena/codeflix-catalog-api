# pylint: disable=attribute-defined-outside-init
from __future__ import annotations

from sqlalchemy.orm.session import Session

from src.data.interfaces import AbstracDbConnectionHandler
from src.infrastructure.db.configs import DEFAULT_SESSION_FACTORY


class DBConnectionHandler(AbstracDbConnectionHandler):
    """Sqlalchemy database connection"""

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
