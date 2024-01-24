import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")



class Test002:
    # @pytest.mark.sanity
    def test_sum_001(self):
        a = 3
        b = 4
        sum = a + b
        print(sum)
        if sum==7:
            assert True
        else:
            assert False

    # @pytest.mark.skip #(for Intentally skip)
    def test_google_002(self):
        driver=webdriver.Chrome()
        # driver=webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo=driver.find_element(By.CLASS_NAME,"lnXdpd").is_displayed()
        print(logo)
        if logo==True:
            driver.close()
            assert True
        else:
            driver.close()
            assert False




