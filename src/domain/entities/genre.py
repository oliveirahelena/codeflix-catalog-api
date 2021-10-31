from typing import Optional

from .entity import Entity


class Genre(Entity):
    """Genre Entity"""

    name: str
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True
