import pytest

class Test003:
    # @pytest.mark.sanity #( markers run to use run specific test cases markers,means decorators  )
    def test_sum_004(self):
        a = 3
        b = 4
        sum = a + b
        print(sum)
        if sum==7:
            assert True
        else: 
            assert False