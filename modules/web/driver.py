from enum import Enum
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

class BROWSER(Enum):
    FIREFOX = 'Firefox'
    CHROME = 'Chrome'
    SAFARI = 'Safari'

class WebDriverCreator():
    def __init__(self):
        pass

    def createDriver(self,browser: BROWSER):
        service = Service()

        # No match-case in python 3.9
        if browser == BROWSER.FIREFOX:
            options = webdriver.FirefoxOptions()
            return webdriver.Firefox(service=service, options=options)
        
        elif browser == BROWSER.CHROME:
            options = webdriver.ChromeOptions()
            return webdriver.Chrome(service=service, options=options)
        
        elif browser == BROWSER.SAFARI:
            options = webdriver.SafariOptions()
            return webdriver.Safari(service=service, options=options)
        
        else:
            raise RuntimeError('[Web Driver]: Unsupported browser or bad input in creator.')
        
