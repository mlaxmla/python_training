__author__ = 'mla'
import pytest
from fixture.application import Application


@pytest.fixture
# @pytest.fixture(scope = "session") - how to fix it?

def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
