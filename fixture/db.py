__author__ = 'mla'
import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password, autocommit=True)
        mysql.connector.connect()

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                all_phones = "\n".join((home, mobile, work, phone2))
                all_emails = "\n".join((email, email2, email3))
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                [group_id] = row
                list.append(Group(id=str(group_id)))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()
