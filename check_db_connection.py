__author__ = 'mla'

# import pymysql.cursors
# 2 import mysql.connector
# 3 from fixture.db import DbFixture
# 4 SPRAWDZAMY ORM dla groups
from fixture.orm import ORMFixture
# 5 SPRAWDZAMY ORM dla contacts
# 6 SPRAWDZAMY ORM dla contacts in group
from model.group import Group
# 7 SPRAWDZAMY ORM dla get_contacts_not_in_group

# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# 2 connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# 3 db = DbFixture(host="127.0.0.1", database="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    # 2 cursor = connection.cursor()
    # 2 cursor.execute("select * from group_list")
    # 2 for row in cursor.fetchall():
    # 2     print(row)
    # groups = db.get_group_list()
    # for group in groups:
    #    print(group)
    # print(len(groups))
    # 3 contacts = db.get_contact_list()
    # 3 for contact in contacts:
    # 3    print(contact)
    # 3 print(len(contacts))
    # 4 l = db.get_group_list()
    # 4 for item in l:
    # 4     print(item)
    # 4 print(len(l))
    # 5 l = db.get_contact_list()
    # 5 for item in l:
    # 5     print(item)
    # 5 print(len(l))
    # 6 l = db.get_contacts_in_group(Group(id="136"))
    # 6 for item in l:
    # 6     print(item)
    # 6 print(len(l))
    l = db.get_contacts_not_in_group(Group(id="136"))
    for item in l:
        print(item)
    print(len(l))
finally:
    # 2 connection.close()
    pass # db.destroy()