__author__ = 'mla'

from model.contact import Contact
from model.group import Group
import random
from random import randrange


def test_del_contact_from_group(app, db):
    add_contact = Contact(firstname="bbb", middlename="aaa", lastname="ccc", nickname="dddd", title="vvvvv", company="bbbbb", address="aaaabbbbb", home="vvvvvbbbbb", mobile="123123123", work="ffffvvvv", fax="222333444", email="a@b.xy", email2="h@k.lm", email3="all@laa.aa", homepage="no", bday="11", bmonth="April", byear="1995", aday="1", amonth="May", ayear="1954", new_group="[none]", address2="zzzz", phone2="132435", notes="ggttyyhh")
    if len(db.get_contact_list()) == 0:
        app.contact.utworz(add_contact)
        print("\nDodano kontakt")
    if len(db.get_group_list()) == 0:
        app.group.utworz(Group(name="abc"))
        print("\nDodano grupę")
    if len(db.get_contacts_in_group()) == 0:
        # wybranie kontaktu bez grupy i dodanie do grupy
        contacts = db.get_contacts_not_in_group()
        contact = random.choice(contacts)
        app.contact.wybierz_kontakt_id(contact.id)
        groups = db.get_group_list()
        group = random.choice(groups)
        app.contact.choose_group_for_contact_by_id(group.id)
        print("\nDodano kontakt do grupy")
    # wybieram grupę z kontaktami
    all_groups = db.get_contacts_in_group()
    chosen_group = random.choice(all_groups)
    app.contact.choose_group_for_contact_del_by_id(chosen_group.id)
    all_contacts_in_group = db.get_contacts_in_group()
    index = randrange(app.contact.count_contacts_in_choosen_group())
    app.contact.choose_contact_by_index(index)
    app.contact.del_contact_from_group()
    print("\nUsunięto kontakt z grupy")
    new_contacts_in_group = db.get_contacts_in_group()
    assert len(all_contacts_in_group) - 1 == len(new_contacts_in_group)
