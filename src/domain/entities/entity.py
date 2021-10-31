import dataclasses
import uuid
from datetime import datetime
from typing import Optional


@dataclasses.dataclass
class Entity:
    """Main class to Entities"""

    id: Optional[uuid.UUID] = uuid.uuid4()
    created_at: Optional[datetime] = datetime.utcnow()
    updated_at: Optional[datetime] = datetime.utcnow()
    deleted_at: Optional[datetime] = None

    @classmethod
    def from_dict(cls, dict_object):
        """Transform a dict to Entity"""

        return cls(**dict_object)

    def to_dict(self):
        """Transform an Entity to Dict"""

        return dataclasses.asdict(self)
