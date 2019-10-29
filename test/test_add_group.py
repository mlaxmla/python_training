# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.groups_with_constant import constant as testdata


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group, db):
    old_groups = db.get_group_list()
    group = Group(name="qqqqqq", header="wwwww", footer="eeeeee")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
