import pytest


# @pytest.mark.xfail #( These marker is use to expected to fail)
class Test004:

    def test_sum_005(self):
        a = 3
        b = 4
        sum = a + b
        print(sum)
        if sum==7:
            assert True
        else:
            assert False
