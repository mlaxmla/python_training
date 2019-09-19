# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="ą1ś", header="b1b", footer="c1c"))
    app.session.logout()