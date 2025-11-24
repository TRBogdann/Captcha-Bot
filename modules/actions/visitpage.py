from .action import AbstractBotAction
from selenium.webdriver.remote.webdriver import WebDriver

class VisitPageAction(AbstractBotAction):
    def __init__(self,driver: WebDriver,url):
        self.driver = driver
        self.url = url
    
    def startAction(self):
        self.driver.get(self.url)
        super().startAction()