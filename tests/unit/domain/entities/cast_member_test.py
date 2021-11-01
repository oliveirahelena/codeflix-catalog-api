import uuid

import pytest

from src.domain.entities import CastMember, CastMemberTypes


def test_cast_member_model_init():
    id = uuid.uuid4()
    cast_member = CastMember(id, name="CastMember 1", type=CastMemberTypes.actor)

    assert cast_member.id == id
    assert cast_member.name == "CastMember 1"
    assert cast_member.type == CastMemberTypes.actor


def test_cast_member_model_post_init():
    id = uuid.uuid4()
    with pytest.raises(TypeError):
        CastMember(id, type=CastMemberTypes.actor)


def test_cast_member_model_from_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "name": "CastMember 1",
        "type": CastMemberTypes.actor,
    }

    cast_member = CastMember.from_dict(init_dict)

    assert cast_member.id == id
    assert cast_member.name == "CastMember 1"
    assert cast_member.type == CastMemberTypes.actor


def test_cast_member_model_to_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "name": "CastMember 1",
        "type": CastMemberTypes.actor,
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    }

    cast_member = CastMember.from_dict(init_dict)

    assert cast_member.to_dict() == init_dict


def test_cast_member_model_comparison():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "name": "CastMember 1",
        "type": CastMemberTypes.actor,
        "created_at": None,
        "updated_at": None,
        "deleted_at": None,
    }

    cast_member1 = CastMember.from_dict(init_dict)
    cast_member2 = CastMember.from_dict(init_dict)

    assert cast_member1 == cast_member2
