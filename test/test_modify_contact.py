__author__ = 'mla'
from model.contact import Contact
import random


#def test_modify_first_contact_firstname(app, db):
#    if len(db.get_contact_list()) == 0:
#        app.contact.create(Contact(firstname="WarunkowoDodany"))
#    old_contacts = db.get_contact_list()
#    contact = Contact(firstname="New firstname")
#    contact.id = old_contacts[0].id
#    if contact.lastname is None:
#        contact.lastname = old_contacts[0].lastname
#    if contact.firstname is None:
#        contact.firstname = old_contacts[0].firstname
#    app.contact.modify_first_contact(contact)
#    assert len(old_contacts) == app.contact.count()
#    new_contacts = db.get_contact_list()
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_some_contact_firstname(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="WarunkowoDodany"))
    old_contacts = db.get_contact_list()
    chosen_contact = random.choice(old_contacts)
    edit_contact = Contact(firstname="Troll")
    # contact = Contact(firstname="New firstname")
    # contact.id = old_contacts[index].id
    # if contact.lastname is None:
    #     contact.lastname = old_contacts[index].lastname
    # if contact.firstname is None:
    #     contact.firstname = old_contacts[index].firstname
    app.contact.modify_contact_by_id(chosen_contact.id, edit_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="WarunkowoDodany"))
    old_contacts = db.get_contact_list()
    chosen_contact = random.choice(old_contacts)
    edit_contact = Contact(firstname="Troll", middlename="Macius", lastname="Ostatni") # middlename="Macius", lastname="Ostatni"
    app.contact.modify_contact_by_id(chosen_contact.id, edit_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

#def test_modify_first_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="WarunkowoDodany"))
#    old_contacts = app.contact.get_contacts_list()
#    contact = Contact(middlename="Zmieniony middlename")  # lastname="Zmieniony lastname", firstname="Zmieniony firstname"
#    contact.id = old_contacts[0].id
#    if contact.lastname is None:
#        contact.lastname = old_contacts[0].lastname
#    if contact.firstname is None:
#        contact.firstname = old_contacts[0].firstname
#    app.contact.modify_first_contact(contact)
#    assert len(old_contacts) == app.contact.count()
#    new_contacts = app.contact.get_contacts_list()
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_some_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="WarunkowoDodany"))
#    old_contacts = app.contact.get_contacts_list()
#    index = randrange(len(old_contacts))
#    contact = Contact(middlename="Zmieniony middlename")  # lastname="Zmieniony lastname", firstname="Zmieniony firstname"
#    contact.id = old_contacts[index].id
#    if contact.lastname is None:
#        contact.lastname = old_contacts[index].lastname
#    if contact.firstname is None:
#        contact.firstname = old_contacts[index].firstname
#    app.contact.modify_contact_by_index(index, contact)
#    assert len(old_contacts) == app.contact.count()
#    new_contacts = app.contact.get_contacts_list()
#    old_contacts[index] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
