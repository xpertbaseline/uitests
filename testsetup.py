from locators import *
from utilities import *
from browserSetUp import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSetUp:
    def __init__(self):
        self.utilities = Utilities()
        self.driver = DriverSetup(os.getenv('BROWSER'))
        self.locator = TemperatureLocators
        self.url =  os.getenv('URL')

    def testRun(self):
        self.driver.openWebPage(os.getenv('URL'))
        self.driver.switchFrame(str(self.locator.TEMPERATURE_FRAME))
        self.driver.find_element_by_id(str(self.locator.TEMP_VALUE))

    def getText(self,element):
        return element.text

