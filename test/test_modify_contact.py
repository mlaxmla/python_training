__author__ = 'mla'
from model.contact import Contact
from random import randrange


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="WarunkowoDodany"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="New firstname")
    contact.id = old_contacts[0].id
    if contact.lastname is None:
        contact.lastname = old_contacts[0].lastname
    if contact.firstname is None:
        contact.firstname = old_contacts[0].firstname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_some_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="WarunkowoDodany"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New firstname")
    contact.id = old_contacts[index].id
    if contact.lastname is None:
        contact.lastname = old_contacts[index].lastname
    if contact.firstname is None:
        contact.firstname = old_contacts[index].firstname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="WarunkowoDodany"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(middlename="Zmieniony middlename")  # lastname="Zmieniony lastname", firstname="Zmieniony firstname"
    contact.id = old_contacts[0].id
    if contact.lastname is None:
        contact.lastname = old_contacts[0].lastname
    if contact.firstname is None:
        contact.firstname = old_contacts[0].firstname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_some_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="WarunkowoDodany"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(middlename="Zmieniony middlename")  # lastname="Zmieniony lastname", firstname="Zmieniony firstname"
    contact.id = old_contacts[index].id
    if contact.lastname is None:
        contact.lastname = old_contacts[index].lastname
    if contact.firstname is None:
        contact.firstname = old_contacts[index].firstname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
