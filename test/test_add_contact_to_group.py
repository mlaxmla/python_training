__author__ = 'mla'
from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, db):
    add_contact = Contact(firstname="bbb", middlename="aaa", lastname="ccc", nickname="dddd", title="vvvvv", company="bbbbb", address="aaaabbbbb", home="vvvvvbbbbb", mobile="123123123", work="ffffvvvv", fax="222333444", email="a@b.xy", email2="h@k.lm", email3="all@laa.aa", homepage="no", bday="11", bmonth="April", byear="1995", aday="1", amonth="May", ayear="1954", new_group="[none]", address2="zzzz", phone2="132435", notes="ggttyyhh")
    if len(db.get_contact_list()) == 0:
        app.contact.create(add_contact)
        print("\nDodano kontakt")
    if len(db.get_group_list()) == 0: # zoptymalizowane: app.group.count() == 0:
        app.group.create(Group(name="test"))
        print("\nDodano grupę")
    all_contacts = db.get_contact_list()
    choosen_contact = random.choice(all_contacts)
    app.contact.choose_contact_by_id(choosen_contact.id)
    all_groups = db.get_group_list()
    choosen_group = random.choice(all_groups)
    old_contacts_in_group = db.get_contacts_in_group()
    app.contact.choose_group_for_contact_by_id(choosen_group.id)
    new_contacts_in_group = db.get_contacts_in_group()
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
    print("\nWybrany kontakt:", choosen_contact)
    print("\nWybrana grupa:", choosen_group)
    print("Przed dodaniem:", len(old_contacts_in_group))
    print("Po dodaniu:",len(new_contacts_in_group))
