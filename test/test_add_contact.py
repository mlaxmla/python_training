# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="aaa", middlename="bbbb", lastname="cccc", nickname="dddd", title="eeee", company="ffff", address="ggggg", home="hhhhhh", mobile="iiii", work="jjjj", fax="kkkk", email="a@q.d", email2="b@w.g", email3="c@h.d", byear="1943", ayear="1992", address2="aaaa", phone2="hhhh", notes="nnnn", phone="666"))
