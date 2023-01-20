import pytest
from utilities.readproperties import Readconfig
from testcase.conftest import setup
@pytest.mark.usefixtures('setup')
class Main_page(Readconfig):

    def test_button(self):
        pass

