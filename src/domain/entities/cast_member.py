import enum
from dataclasses import dataclass
from typing import Optional

from .entity import Entity


class CastMemberTypes(enum.Enum):
    """Defining Cast Member Types"""

    actor = "actor"
    director = "director"


@dataclass
class CastMember(Entity):
    """CastMember Entity"""

    name: Optional[str] = None
    type: Optional[CastMemberTypes] = CastMemberTypes.actor

    def __post_init__(self):
        if self.name == "" or self.name is None:
            raise TypeError("__init__ missing 1 required argument: 'name'")
