from dataclasses import dataclass, field
from typing import Optional

from .entity import Entity


@dataclass
class Video(Entity):
    """Video Entity"""

    title: Optional[str] = None
    description: Optional[str] = None
    year_launched: Optional[int] = None
    opened: Optional[bool] = field(default=True, init=True)
    rating: Optional[str] = None
    duration: Optional[float] = None
    thumb_file: Optional[str] = None
    banner_file: Optional[str] = None
    trailer_file: Optional[str] = None
    video_file: Optional[str] = None

    def __post_init__(self):
        if self.title == "" or self.title is None:
            raise TypeError("__init__ missing 1 required argument: 'title'")
