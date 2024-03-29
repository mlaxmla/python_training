__author__ = 'mla'
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None, work=None, fax=None, homepage = None, email=None, email2=None, email3=None, address2=None, phone2=None, notes=None, phone=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, id=None, all_phones=None, all_phones_from_home_page=None, all_emails=None, all_emails_from_home_page=None, new_group=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.homepage = homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.phone = phone
        self.id = id
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.all_phones = all_phones
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails = all_emails
        self.all_emails_from_home_page = all_emails_from_home_page
        self.new_group = new_group

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.nickname) # lepiej byłoby tak "%s:%s:%s" % (self.id, self.firstname, self.lastname), ale jeszcze nie umiem podmienić w liście elelemntu o określonym id, a na widoku contacts mamy sortowanie wg lastname, firstname

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname # and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    #def all_phones(self):
    #    return str(self)