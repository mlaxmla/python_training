__author__ = 'mla'
from model.group import Group
import random


#def test_delete_first_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.delete_first_group()
#    assert len(old_groups) - 1 == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups[0:1] = []
#    assert old_groups == new_groups

def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0: # zoptymalizowane: app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    # optymalizacja usuwania w celu dostosowania do wybierania elementu z bazy
    # index = randrange(len(old_groups))
    # app.group.delete_group_by_index(index)
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    # old_groups[index:index+1] = []
    old_groups.remove(group)
    assert old_groups == new_groups
