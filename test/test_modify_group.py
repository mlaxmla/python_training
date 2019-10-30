__author__ = 'mla'
from model.group import Group
import random
import string

def random_string(prefix, maxlen):
   symbols = string.ascii_letters + string.digits + " "*10 # string.punctuation +
   return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip()

#def random_string(maxlen):
#    symbols = string.ascii_letters + string.digits + " " * 10
#    chars = "".join([random.choice(symbols) for i in range(random.randrange(5,maxlen))]).strip()
#    return chars


def test_modify_first_group_name(app, db):
    if len(db.get_contact_list())  == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_contact_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.modify2_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #app.session.logout()

def test_modify_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20)))
    old_groups = db.get_group_list()
    chosen_group = random.choice(old_groups)
    app.group.modify2_group_by_id(chosen_group.id, Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20)))
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    #app.session.logout()
    if check_ui:
        assert len(old_groups) == len(app.group.get_group_list())

#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify2_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
    #app.session.logout()
