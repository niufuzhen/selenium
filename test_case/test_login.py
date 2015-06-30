from main.activity.activity_login import *
from main.activity.activity_logout import *
from main.activity.activity_header import *
from main.activity.activity_inbox_review import *
from main.activity.activity_index import *
from main.lib.user_data import *
from main.function.setup import *
from main.page.base import *
from main.page.header import *
from main.page.index.pe_index import *
import time, platform
import unittest, string, random

class TestLogin(unittest.TestCase):

    #Instance
    _site = "live"


    def setUp(self):

        test_driver = ""
        self.driver = tsetup()
        self.flag = 0


    def test_1_login_success(self):
        print ("TEST #1 : Check Login Success")
        print ("=======================")
        driver = self.driver

        email = user3['email']
        pwd = user3['pwd']

        #Object Activity
        loginValidate = loginActivity()
        logoutValidate = logoutActivity()
        checkInboxReview = inboxReviewActivity()
        checkIndex = indexActivity()
        checkHeader = headerActivity()
        #--

        h_flag = loginValidate.do_login(driver, email, pwd, self._site)
        checkInboxReview.setObject(driver)
        checkInboxReview.goto_inbox_review(self._site)
        checkIndex.now_at_index(driver)
        checkHeader.check_header_status(driver,h_flag)
        logoutValidate.do_logout(driver, self._site)

    def test_2_login_validation_input_empty(self):
        print ("TEST #2 : [Validation] Login Empty")
        print ("==================================")
        driver = self.driver
        loginValidate = loginActivity()
        loginValidate.check_validasi_login_input_empty(driver, self._site)

    def test_3_login_validation_input_email(self):
        print ("TEST #3 : [Validation] Input Email")
        print ("==================================")
        driver = self.driver
        email = user3['email']
        loginValidate = loginActivity()
        loginValidate.check_validasi_input_email(driver, email, self._site)

    def test_4_login_validation_input_password(self):
        print ("TEST #4 : [Validation] Input Password")
        print ("==================================")
        driver = self.driver
        pwd = user3['pwd']
        loginValidate = loginActivity()
        loginValidate.check_validasi_input_password(driver, pwd, self._site)


    def test_5_login_success_at_header(self):
        print ("TEST #5 : Login Success at Index")
        print ("==================================")
        driver = self.driver

        email = user3['email']
        pwd = user3['pwd']

        loginValidate = loginActivityAtHeader()
        doLogout = logoutActivity()

        loginValidate.doLoginAtIndex(driver, self._site, self.flag, email, pwd)
        doLogout.do_logout(driver, self._site)


    def tearDown(self):
        #self.timeend = time.clock()
        #t = self.timeend - self.timestart
        print("Testing akan selesai dalam beberapa saat..")
        self.driver.quit()
        #print ("waktu test : %.3f" %(t))


if __name__ == '__main__':
    unittest.main(warnings='ignore')




