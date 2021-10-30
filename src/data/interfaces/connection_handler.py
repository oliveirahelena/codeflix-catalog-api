# pylint: disable=attribute-defined-outside-init
from __future__ import annotations

import abc


class AbstracDbConnectionHandler(abc.ABC):
    """Abstract database connection"""

    def __enter__(self) -> AbstracDbConnectionHandler:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        """Commit changes in database"""

        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        """Rollback changes in database"""

        raise NotImplementedError
