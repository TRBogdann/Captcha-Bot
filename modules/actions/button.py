from .action import AbstractBotAction
from modules.web.html import HTMLElement

class ButtonPressAction(AbstractBotAction):
    def __init__(self,button: HTMLElement):
        self.button = button
    
    def startAction(self):
        self.button.WebElement().click()
        super().startAction()