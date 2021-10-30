import dataclasses
import uuid


@dataclasses.dataclass
class Entity:
    id: uuid.UUID

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
