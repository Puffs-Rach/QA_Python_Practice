# pytest is widely used
# plain assert statements
#flexible and has good integration


import 
from pytest_files.my_functions import *

def test_answer(): # make a function with test_, assert statemtnts. when we call add, it should result
    result = add(1,2)
    assert add(1,2) == 3
    assert add(1, 2) == 1 + 2
    assert result == 3


# class based testing

class test_area:
    def setup_method(self):
        self.x = Area(5,10)

    def area_calc(self):
        assert self.x.area_calc() == 50

    def teardown_method(self):
        del self.x


# fixtures in pytestp