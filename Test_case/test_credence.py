import time
import unittest



from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome_options = webdriver.ChromeOptions()
# Chrome_options.add_argument("headless") #(with Headleass)


class TestCredence(unittest.TestCase):

    def test_credence_008(self):
        driver = webdriver.Chrome()  # (wihtout headless)
        # driver=webdriver.Chrome(options=Chrome_options)
        driver.get("https://credence.in/")
        time.sleep(1)
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        l = len(driver.find_elements(By.XPATH, "//div[@class ='quickfinder-description gem-text-output']//p//a"))
        # print(l)
        list = []
        for r in range(1, l + 1):
            contact = driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a["+str( r)+"]").text
            list.append(contact)

            if "+91 9091929355" in list:
                self.assertTrue(True)

            else:
                # print(r)
                self.assertFalse(False)





        # if driver.title=="credence":
        #     # driver.close()
        #     assert True
        # else:
        #     # driver.close()
        #     assert False


# To use these code to run parallel test cases (pytest -v --html=reports/reports2.html)
# cls  is use to clear the all matters in the terminal
#( pytest -v --html=reports/report.html -n=6 ) To use test case parelley run( These is mean worker in  processor )
# import unitest library to reduce error in test cases
# import library xdist 


