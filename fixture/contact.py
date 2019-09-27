__author__ = 'mla'
from selenium.webdriver.support.ui import Select
#from fixture.application import Application #ASK4IT: czy tego nie potrzebujemy dzieki temu ze przenieslismy fixtury do conftest.py i 'przedrostek' "app." odwoluje sie do nich?


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
        wd = self.app.wd
        self.open_home_page2() #ASK4IT: jak zrobic aby dzialalo przez "app." z conftest.py? Niech mi to ktos wytlumaczy prosze...
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submin delation
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close alert
        wd.switch_to.alert.accept()
        # home_page opened Application.open_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page2()
        # init first contact edit
        wd.find_element_by_xpath("//a//img[@title='Edit']").click() #  and @xpath='1'
        #self.modify(new_group_data)
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()

    def modify(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        # submit update
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page2()
        return len(wd.find_elements_by_name("selected[]"))