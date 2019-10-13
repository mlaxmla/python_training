__author__ = 'mla'
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

# from fixture.application import Application #ASK4IT: czy tego nie potrzebujemy dzieki temu ze przenieslismy fixtury do conftest.py i 'przedrostek' "app." odwoluje sie do nich?


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page2(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.get("http://localhost/addressbook/")

    def create(self, contact):
        wd = self.app.wd
        # init new-contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("firstname", contact.firstname)
        # to-do
        #wd.find_element_by_name("bday").click()
        #Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        #wd.find_element_by_xpath("//option[@value='1']").click()
        #wd.find_element_by_name("bmonth").click()
        #Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        #wd.find_element_by_xpath("//option[@value='June']").click()
        self.change_field_value("byear", contact.byear)
        # to-do
        #wd.find_element_by_name("aday").click()
        #Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
        #wd.find_element_by_css_selector("select[name=\"aday\"] > option[value=\"2\"]").click()
        #wd.find_element_by_name("amonth").click()
        # to-do
        #Select(wd.find_element_by_name("amonth")).select_by_visible_text("August")
        #wd.find_element_by_xpath("(//option[@value='August'])[2]").click()
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        # wd.find_element_by_name("phone").clear()
        # wd.find_element_by_name("phone").send_keys(contact.phone)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page2() #ASK4IT: jak zrobic aby dzialalo przez "app." z conftest.py? Niech mi to ktos wytlumaczy prosze...
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submin delation
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close alert
        wd.switch_to.alert.accept()
        # home_page opened Application.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page2()
        # init first contact edit
        wd.find_elements_by_xpath("//a//img[@title='Edit']")[index].click() #  and @xpath='1'
        #self.modify(new_group_data)
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        # submit update
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page2()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page2()
            self.contact_cache = []
            r = 1
            for element in wd.find_elements_by_xpath("//*[@name='entry']"): # "//a//img[@title='Edit']"
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname_text = element.find_element_by_xpath("//*[@id='maintable']/tbody/tr["+str(r+1)+"]/td[2]").text
                firstname_text = element.find_element_by_xpath("//*[@id='maintable']/tbody/tr["+str(r+1)+"]/td[3]").text
                all_phones_from_contactlist = element.find_element_by_xpath("//*[@id='maintable']/tbody/tr["+str(r+1)+"]/td[6]").text.splitlines()
                all_phones = element.find_element_by_xpath("//*[@id='maintable']/tbody/tr[" + str(r + 1) + "]/td[6]").text
                r = r + 1
                self.contact_cache.append(Contact(lastname=lastname_text, firstname=firstname_text, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_all_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page2()
            self.contact_cache = []
            r = 1
            for element in wd.find_elements_by_xpath("//*[@name='entry']"): # "//a//img[@title='Edit']"
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname_text = element.find_element_by_xpath("//*[@id='maintable']/tbody/tr["+str(r+1)+"]/td[2]").text
                firstname_text = element.find_element_by_xpath("//*[@id='maintable']/tbody/tr["+str(r+1)+"]/td[3]").text
                address_text = element.find_element_by_xpath("//*[@id='maintable']/tbody/tr["+str(r+1)+"]/td[4]").text
                all_emails = element.find_element_by_xpath("//*[@id='maintable']/tbody/tr[" + str(r + 1) + "]/td[5]").text
                all_phones = element.find_element_by_xpath("//*[@id='maintable']/tbody/tr[" + str(r + 1) + "]/td[6]").text
                r = r + 1
                self.contact_cache.append(Contact(lastname=lastname_text, firstname=firstname_text, id=id, address=address_text, all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    #how2FIX-IT-Alexei?
    #def get_contacts_list_webinar(self):
    #    if self.contact_cache is None:
    #        wd = self.app.wd
    #        self.open_home_page2()
    #        self.contact_cache = []
    #        for row in wd.find_elements_by_name("entry"):
    #            cells = row.find_elements_by_tag_name("td")
    #            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
    #            firstname_text = cells[1].text
    #            lastname_text = cells[2].text
    #            self.contact_cache.append(Contact(lastname=lastname_text, firstname=firstname_text, id=id))
    #    return list(self.contact_cache)


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page2()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page2()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def clear(self, s):
        return re.sub("[() -=]", "", s)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = (None if wd.find_element_by_name("home").get_attribute("value") == "" else wd.find_element_by_name("home").get_attribute("value"))
        work = (None if wd.find_element_by_name("work").get_attribute("value") == "" else wd.find_element_by_name("work").get_attribute("value"))
        mobile = (None if wd.find_element_by_name("mobile").get_attribute("value") == "" else wd.find_element_by_name("mobile").get_attribute("value"))
        phone2 = (None if wd.find_element_by_name("phone2").get_attribute("value") == "" else wd.find_element_by_name("phone2").get_attribute("value"))
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, work=work, mobile=mobile, phone2=phone2) # all_phones=all_phones_from_edit_witohout_nulls

    def get_all_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = (None if wd.find_element_by_name("home").get_attribute("value") == "" else wd.find_element_by_name("home").get_attribute("value"))
        work = (None if wd.find_element_by_name("work").get_attribute("value") == "" else wd.find_element_by_name("work").get_attribute("value"))
        mobile = (None if wd.find_element_by_name("mobile").get_attribute("value") == "" else wd.find_element_by_name("mobile").get_attribute("value"))
        phone2 = (None if wd.find_element_by_name("phone2").get_attribute("value") == "" else wd.find_element_by_name("phone2").get_attribute("value"))
        address = (None if wd.find_element_by_name("address").get_attribute("value") == "" else wd.find_element_by_name("address").get_attribute("value"))
        email = (None if wd.find_element_by_name("email").get_attribute("value") == "" else wd.find_element_by_name("email").get_attribute("value"))
        email2 = (None if wd.find_element_by_name("email2").get_attribute("value") == "" else wd.find_element_by_name("email2").get_attribute("value"))
        email3 = (None if wd.find_element_by_name("email3").get_attribute("value") == "" else wd.find_element_by_name("email3").get_attribute("value"))
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, work=work, mobile=mobile, phone2=phone2, address=address, email=email, email2=email2, email3=email3) # all_phones=all_phones_from_edit_witohout_nulls

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = (None if re.search("H: (.*)", text) is None else re.search("H: (.*)", text).group(1))
        work = (None if re.search("W: (.*)", text) is None else re.search("W: (.*)", text).group(1))
        mobile = (None if re.search("M: (.*)", text) is None else re.search("M: (.*)", text).group(1))
        phone2 = (None if re.search("P: (.*)", text) is None else re.search("P: (.*)", text).group(1))
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2) # home=home, work=work, mobile=mobile, phone2=phone2 # firstname=firstname, lastname=lastname, id=id, all_phones=all_phones_from_edit_witohout_nulls
