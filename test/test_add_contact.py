# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="aaa", middlename="bbbb", lastname="cccc", nickname="dddd", title="eeee", company="ffff", address="ggggg", home="hhhhhh", mobile="iiii", work="jjjj", fax="kkkk", email="a@q.d", email2="b@w.g", email3="c@h.d", byear="1943", ayear="1992", address2="aaaa", phone2="hhhh", notes="nnnn", phone="666"))
    app.logout()
