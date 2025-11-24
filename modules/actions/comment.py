from modules.actions import AbstractBotAction
from modules.web.html import HTMLElement

class WriteCommentAction(AbstractBotAction):
    def __init__(self,comment:str,textField:HTMLElement,sendButton: HTMLElement):
        self.comment = comment
        self.sendButton = sendButton
        self.textField = textField

    def startAction(self):
        self.textField.WebElement().send_keys(self.comment)
        self.sendButton.WebElement().click(self.comment)
        super().startAction()