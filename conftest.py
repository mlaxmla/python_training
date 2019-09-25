__author__ = 'mla'
import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
# @pytest.fixture(scope = "session") - how to fix it?
# all test pass without '(scope = "session")'
# tests which don't pass with '(scope = "session")': test_mod_contact, test_modify_contact_firstname, test_modify_contact_middlename
# why do they fail or why the others pass?
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
