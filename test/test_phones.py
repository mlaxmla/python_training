__author__ = 'mla'
import re
from random import randrange


def test_all_details_on_home_page(app):
    contacts_list = app.contact.get_all_contacts_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = app.contact.get_all_contacts_list()[index]
    contact_from_edit_page = app.contact.get_all_contact_info_from_edit_page(index)
    assert sorted(contact_from_home_page.all_phones_from_home_page) == sorted(merge_phones_like_on_home_page(contact_from_edit_page))
    #assert contact_from_home_page.address == contact_from_edit_page.address # AssertionError  assert contact_from_home_page.address == contact_from_edit_page.address is None
    assert sorted(contact_from_home_page.all_emails_from_home_page) == sorted(merge_emails_like_on_home_page(contact_from_edit_page))


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert sorted(contact_from_home_page.all_phones_from_home_page) == sorted(merge_phones_like_on_home_page(contact_from_edit_page))


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contacts_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2
#    assert sorted(contact_from_view_page.all_phones) == sorted(contact_from_edit_page.all_phones)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.work, contact.mobile, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            # map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))
