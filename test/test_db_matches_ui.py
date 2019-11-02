__author__ = 'mla'
from model.group import Group
from model.contact import Contact
from timeit import timeit


def test_group_list(app, db):
    # print(timeit(lambda: app.group.get_group_list(), number=1))
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    # db_list_temp = db.get_group_list()
    # print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    db_list = map(clean, db.get_group_list())
    # assert False
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_contact_list(app, db):
    ui_contact_list = app.contact.get_all_contacts_list()
    # print(timeit(lambda: app.contact.get_contact_list(), number=1))
    db_contact_list = db.get_contact_list()
    # elements at lists are equal (I've checked few) - WHY it doesn't work? Maybe it needs some deeper cleaning or some changes in model/contact/__eq__?? I'm lost...
    assert sorted(ui_contact_list, key=Group.id_or_max) == sorted(db_contact_list, key=Group.id_or_max)
