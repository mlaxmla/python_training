# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_contact(app):
    app.contact.modify_first_contact(Contact(firstname="zzz", middlename="yyy", lastname="xxx", nickname="iii", title="a a a", company="ttt", address="gg", home="hhhhhh", mobile="iiii", work="jjjj", fax="kkkk", email="a@q.d", email2="b@w.g", email3="c@h.d", byear="1943", ayear="1992", address2="aaaa", phone2="hhhh", notes="nnnn", phone="666"))
