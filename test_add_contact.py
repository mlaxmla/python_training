# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd)
        # logout
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, wd):
        # init new-contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("aaa")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("bbbb")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("cccc")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("dddd")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("eeee")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("ffff")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("ggggg")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("hhhh")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("iiii")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("jjjj")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("kkkk")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("a@q.d")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("b@w.g")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("c@h.d")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_xpath("//option[@value='June']").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1943")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("2")
        wd.find_element_by_css_selector("select[name=\"aday\"] > option[value=\"2\"]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("August")
        wd.find_element_by_xpath("(//option[@value='August'])[2]").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1992")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("aaaa")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("hhhh")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("nnnn")
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
