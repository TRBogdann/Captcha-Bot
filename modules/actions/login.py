from .action import AbstractBotAction
from modules.captcha.readers.captcha_reader import CaptchaReader
from modules.web.html import HTMLElement

class LogInAction(AbstractBotAction):
    def __init__(self, 
                emailField: HTMLElement,
                passwordField: HTMLElement,
                email: str ,
                password: str, 
                submitButton: HTMLElement = None,
                captchaField: HTMLElement = None,
                captchaElement: HTMLElement = None,
                captchaReader: CaptchaReader = None, 
):
        self.emailField = emailField
        self.passwordField = passwordField
        self.password = password
        self.email = email
        self.submitButton = submitButton
        self.captchaReader = captchaReader
        self.captchaElement = captchaElement
        self.captchaField = captchaField

    def startAction(self):
        self.emailField.WebElement().send_keys(self.email)
        self.passwordField.WebElement().send_keys(self.password)

        if self.captchaReader and self.captchaElement and self.captchaField:
            decoded = self.captchaReader.read(self.captchaElement)
            self.captchaField.WebElement().send_keys(decoded)
        
        if self.submitButton:
            self.submitButton.WebElement().click()

        super().startAction()