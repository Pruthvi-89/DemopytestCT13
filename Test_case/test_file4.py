import pytest

class Test_py:

    def test_0006(self):
        x=5
        y=7
        mul=x*y
        print(mul)
        if mul==35:
          assert True
        else:
            assert False

# pytest -v  to use details test cases
# pytest  - m(markername) to use run specific group test cases
# pytest -v --html=report.html (to use create html reports )