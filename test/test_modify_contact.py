__author__ = 'mla'
from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="New middlename"))
