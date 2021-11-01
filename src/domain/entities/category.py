from dataclasses import dataclass, field
from typing import Optional

from .entity import Entity


@dataclass
class Category(Entity):

    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = field(default=True, init=True)

    def __post_init__(self):
        if self.name == "" or self.name is None:
            raise TypeError("__init__ missing 1 required argument: 'name'")
