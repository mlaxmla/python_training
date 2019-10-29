__author__ = 'mla'
from model.contact import Contact
import random


def test_delete_first_contact(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="WarunkowoDodany"))
    old_contacts = db.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    # new_contacts = db.get_contact_list()
    # del old_contacts[0]
    # old_contacts[0:1] = []
    # assert old_contacts == new_contacts


def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="WarunkowoDodany"))
    # old_contacts = app.contact.get_contacts_list()
    old_contacts = db.get_contact_list()
    # optymalizacja usuwania w celu dostosowania do wybierania elementu z bazy
    # index = randrange(len(old_contacts))
    # app.contact.delete_contact_by_index(index)
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    # old_contacts[index:index+1] = []
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
