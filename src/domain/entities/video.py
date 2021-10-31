from .entity import Entity


class Video(Entity):
    """Video Entity"""

    title: str
    description: str
    year_launched: int
    opened: bool
    rating: str
    duration: int
    thumb_file: str
    banner_file: str
    trailer_file: str
    video_file: str

    class Config:
        orm_mode = True
