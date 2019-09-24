__author__ = 'mla'
import pytest
from fixture.application import Application


@pytest.fixture
# @pytest.fixture(scope = "session") - how to fix it?
# all test pass without '(scope = "session")'
# tests which don't pass with '(scope = "session")': test_mod_contact, test_modify_contact_firstname, test_modify_contact_middlename
# why do they fail or why the others pass?
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
