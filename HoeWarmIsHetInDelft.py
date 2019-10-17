from testsetup import *
testsetup = TestSetUp()
driverSetUp = testsetup.driver
driverSetUp.openWebPage(os.getenv('URL'))
driverSetUp.switchFrame(str(testsetup.locator.TEMPERATURE_FRAME))
tempFromBrowser = driverSetUp.getElement(str(testsetup.locator.TEMP_VALUE)).text
removeDegFromTemp = tempFromBrowser.split(tempFromBrowser[-2:])
roundedCelsius = round(float(removeDegFromTemp[0]))
print(str(roundedCelsius) + " degrees Celsius")
assert roundedCelsius is not None
driverSetUp.browserClose()
