import uuid

import pytest

from src.domain.entities import Video


def test_video_model_init():
    id = uuid.uuid4()
    video = Video(
        id,
        title="Patrulha Canina",
        description="Cães falantes usam equipamentos para resolver crimes",
        year_launched=2021,
        opened=True,
        rating="4",
        duration=1.5,
        thumb_file="thumb.jpg",
        banner_file="banner.jpg",
        trailer_file="trailer.mp4",
        video_file="video.mp4",
    )

    assert video.id == id
    assert video.title == "Patrulha Canina"
    assert video.description == "Cães falantes usam equipamentos para resolver crimes"
    assert video.year_launched == 2021
    assert video.opened is True
    assert video.rating == "4"
    assert video.duration == 1.5
    assert video.thumb_file == "thumb.jpg"
    assert video.banner_file == "banner.jpg"
    assert video.trailer_file == "trailer.mp4"
    assert video.video_file == "video.mp4"


def test_video_model_post_init():
    id = uuid.uuid4()
    with pytest.raises(TypeError):
        Video(id, description="Descrição do Video 1")


def test_video_model_from_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "title": "Patrulha Canina",
        "description": "Cães falantes usam equipamentos para resolver crimes",
        "year_launched": 2021,
        "opened": True,
        "rating": "4",
        "duration": 1.5,
        "thumb_file": "thumb.jpg",
        "banner_file": "banner.jpg",
        "trailer_file": "trailer.mp4",
        "video_file": "video.mp4",
    }

    video = Video.from_dict(init_dict)

    assert video.id == id
    assert video.title == "Patrulha Canina"
    assert video.description == "Cães falantes usam equipamentos para resolver crimes"
    assert video.year_launched == 2021
    assert video.opened is True
    assert video.rating == "4"
    assert video.duration == 1.5
    assert video.thumb_file == "thumb.jpg"
    assert video.banner_file == "banner.jpg"
    assert video.trailer_file == "trailer.mp4"
    assert video.video_file == "video.mp4"


def test_video_model_to_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "title": "Patrulha Canina",
        "description": "Cães falantes usam equipamentos para resolver crimes",
        "year_launched": 2021,
        "opened": True,
        "rating": "4",
        "duration": 1.5,
        "thumb_file": "thumb.jpg",
        "banner_file": "banner.jpg",
        "trailer_file": "trailer.mp4",
        "video_file": "video.mp4",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    }

    video = Video.from_dict(init_dict)

    assert video.to_dict() == init_dict


def test_video_model_comparison():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "title": "Patrulha Canina",
        "description": "Cães falantes usam equipamentos para resolver crimes",
        "year_launched": 2021,
        "opened": True,
        "rating": "4",
        "duration": 1.5,
        "thumb_file": "thumb.jpg",
        "banner_file": "banner.jpg",
        "trailer_file": "trailer.mp4",
        "video_file": "video.mp4",
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    }

    video1 = Video.from_dict(init_dict)
    video2 = Video.from_dict(init_dict)

    assert video1 == video2
