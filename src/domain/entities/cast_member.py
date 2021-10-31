import enum

from .entity import Entity


class CastMemberTypes(enum.Enum):
    """Defining Cast Member Types"""

    actor = "actor"
    director = "director"


class CastMember(Entity):
    """CastMember Entity"""

    name: str
    type: CastMemberTypes

    class Config:
        orm_mode = True
