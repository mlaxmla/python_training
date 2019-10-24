__author__ = 'mla'

# import pymysql.cursors
# 2 import mysql.connector
from fixture.db import DbFixture

# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# 2 connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = DbFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    # 2 cursor = connection.cursor()
    # 2 cursor.execute("select * from group_list")
    # 2 for row in cursor.fetchall():
    # 2     print(row)
    # groups = db.get_group_list()
    # for group in groups:
    #    print(group)
    # print(len(groups))
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    # 2 connection.close()
    db.destroy()