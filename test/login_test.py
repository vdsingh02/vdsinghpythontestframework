from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import Utils as utils
import moment
import allure

@pytest.mark.usefixtures("test_setup")

class TestLogin():


    def test_login(self):
        driver= self.driver
        driver.get(utils.URL)

        login=LoginPage(driver)
        login.enter_username(utils.Username)
        login.enter_password(utils.Password)
        login.click_login()
        driver.implicitly_wait(10)


    def test_logout(self):
        try:
            driver= self.driver
            homepage1=HomePage(driver)
            homepage1.click_welcome()
            homepage1.click_logout()
            x=driver.title
            assert x == "abc"
            #assert x == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currTime=moment.now().strftime("%d-%m-%y_%H-%M-%S")
            testName=utils.whoami()
            screenshotName=testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),screenshotName,attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/Users/vdsingh/PycharmProjects/vikashtestframework/screenshots/" + screenshotName + ".png")
            raise
        except:
            print("There was an exceptiom")

            currTime = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            raise
        else:
            print("There was no error")

        finally:
            print("I am inside final block")




