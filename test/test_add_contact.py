# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
   symbols = string.ascii_letters + string.digits + " "*10 # string.punctuation +
   return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
            address="", home="", mobile="", work="", fax="", email="", email2="",
            email3="", byear="", ayear="", address2="", phone2="", notes="", phone="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20), nickname=random_string("nickname", 20), title=random_string("title", 20), company=random_string("company", 20),
            address=random_string("address", 20), home=random_string("home", 20), mobile=random_string("mobile", 20), work=random_string("work", 20), fax=random_string("fax", 20), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20), byear=random_string("byear", 20), ayear=random_string("ayear", 20), address2=random_string("address2", 20), phone2=random_string("phone2", 20), notes=random_string("notes", 20), phone=random_string("phone", 20))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
