
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverSetup:
    driver = None
    def __init__(self,browser):
        self.browser = browser
        self.getDriver()

# We can add other browser options here
# using docker compose to run these tests else we need to have chrome and selenium installed and also point to the chrome path
# hardcoded selenium-hub but these can be added as an env variable in docker-compose and we can use it here
    def getDriver(self):
          if self.driver == None:
            if self.browser == "remote":
                 self.driver = webdriver.Remote(
                                  command_executor='http://selenium-hub:4444/wd/hub',
                                  desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
            elif self.browser == "chrome" :
                 print(self.browser)
                 self.driver = webdriver.Chrome()
            else:
                 self.driver = webdriver.Firefox()
          return self.driver

# We can add another param locatorType and based on the locator type wait for the element.locatorType
# For the case of simplicity we are using CSS_SELECTOR
    def getWebDriverWait(self, elementLocator):
          waitForElement = WebDriverWait(self.driver, 15)
          waitForElement.until(EC.presence_of_element_located((By.CSS_SELECTOR, elementLocator)))

# We can add another param locatorType and based on the locator type wait for the element.locatorType
# For the case of simplicity we are using CSS_SELECTOR
    def switchFrame(self,css_selector):
          self.driver.switch_to.frame(self.driver.find_element_by_css_selector(css_selector))

    def getElement(self,css_selector):
          return self.driver.find_element_by_css_selector(css_selector)

# Closing the browser
    def browserClose(self):
        self.driver.close()
        self.driver.quit()
# open the webpage
    def openWebPage(self,webPage):
        self.driver.get(webPage)
        self.driver.maximize_window()




