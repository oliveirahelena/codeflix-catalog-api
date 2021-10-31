from dataclasses import dataclass, field
from typing import Optional

from .entity import Entity


@dataclass
class Category(Entity):
    """Category Entity"""

    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = field(default=True, init=True)

    def __post_init__(self):
        for key, value in self.__dict__.items():
            if key == "name" or key == "description":
                if value == "" or value is None:
                    raise TypeError(f"__init__ missing 1 required argument: '{key}'")
