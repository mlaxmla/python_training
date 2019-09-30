# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="aaa", middlename="bbbb", lastname="cccc", nickname="dddd", title="eeee", company="ffff",
            address="ggggg", home="hhhhhh", mobile="iiii", work="jjjj", fax="kkkk", email="a@q.d", email2="b@w.g",
            email3="c@h.d", byear="1943", ayear="1992", address2="aaaa", phone2="hhhh", notes="nnnn", phone="666")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
