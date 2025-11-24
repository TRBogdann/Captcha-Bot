from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from collections.abc import Callable

class HTMLElement():
    def __init__(self, driver:WebDriver,findBy: By, identifier: any):
        self.driver = driver
        self.findBy = findBy
        self.identifier = identifier
        self._webElement = None
    
    def WebElement(self)->WebElement:
        if self._webElement is None:
            self._webElement = self.driver.find_element(self.findBy,self.identifier)

        return self._webElement


class HTMLElementPromise(HTMLElement):
    def __init__(self, driver: WebDriver, findBy: By, identifier: any, match: Callable[[int,WebElement],bool] ):
        super().__init__(driver,findBy,identifier)
        self.match = match
    
    def WebElement(self):
        if self._webElement is None:
            for index, element in enumerate(self.driver.find_elements(self.findBy,self.identifier)):
                if(self.match(index, element)):
                    self._webElement = element

        return self._webElement


class HTMLElementList():
    def __init__(self, driver:WebDriver,findBy: By, identifier: any):
        self.driver = driver
        self.findBy = findBy
        self.identifier = identifier
        self._elements = None
    
    def items(self):
        if self._elements is None:
            self._elements = self.driver.find_elements(self.findBy,self.identifier)
    