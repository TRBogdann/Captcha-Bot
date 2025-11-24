import os
import tensorflow as tf
import modules.captcha.ocr as ocr
from modules.web.driver import WebDriverCreator,BROWSER
from modules.web.html import HTMLElement,HTMLElementPromise
from modules.actions import BotRoutine
from modules.actions import VisitPageAction,PauseBotAction,RepeatAction,LogInAction,ButtonPressAction,WriteCommentAction
from modules.captcha.readers import ImageCaptchaReader


from dotenv import load_dotenv, dotenv_values 
load_dotenv()

class TestCaptchaBot():
    def __init__(self, model_path, vocabulary_path):
        self.vocabulary = ocr.loadVocabulary(vocabulary_path)
        self.captchaReader = ImageCaptchaReader(model_path,self.vocabulary,200,40)
        self.driver = WebDriverCreator().createDriver(BROWSER(os.getenv('DRIVER')))
        self.auth_url = os.getenv('AUTH_STAGE_URL')
        self.target_page_url = os.getenv('TARGET_PAGE_URL')
        self.home_page_url = os.getenv('HOME_PAGE_URL')

        self.emailField = HTMLElement(self.driver,os.getenv('EMAIL_FIELD_FIND_BY'),os.getenv('EMAIL_FIELD_ID'))
        self.passwordField = HTMLElement(self.driver,os.getenv('PASSWORD_FIELD_FIND_BY'),os.getenv('PASSWORD_FIELD_ID'))
        self.captchaField = HTMLElement(self.driver,os.getenv('CAPTCHA_FIELD_FIND_BY'),os.getenv('CAPTCHA_FIELD_ID'))
        self.captchaImage = HTMLElementPromise(
            self.driver,
            os.getenv('CAPTCHA_GENERATOR_FIND_BY'),
            os.getenv('CAPTCHA_GENERATOR_ID'),
            match = lambda index, element: index == 0
        )
        self.submitButton =  HTMLElementPromise(
            self.driver,
            os.getenv('SUBMIT_BUTTON_FIND_BY'),
            os.getenv('SUBMIT_BUTTON_ID'),
            match = lambda index, element: index == 0
        )

        self.comanda = HTMLElementPromise(
            self.driver,
            os.getenv('COMENZI_FIND_BY'),
            os.getenv('COMENZI_ID'),
            match = lambda index, element: index == 12
        )

        self.commentField = HTMLElementPromise(
            self.driver,
            os.getenv('COMMENT_FIELD_FIND_BY'),
            os.getenv('COMMENT_FIELD_ID'),
            match = lambda index, element: index == 0
        )

        self.submitComment = HTMLElementPromise(
            self.driver,
            os.getenv('COMMENT_SUBMIT_FIND_BY'),
            os.getenv('COMMENT_SUBMIT_ID'),
            match = lambda index, element:  element.text == 'Trimite mesajul'
        )

        self.comment = '[Scam Bot]: Hello. Check the link bellow and win $1000000000000: https://notscam.com'

        self.routine = self._createRoutine()


    def _LogInSubRoutine(self):
        return BotRoutine(
            [
                LogInAction(
                    self.emailField,
                    self.passwordField,
                    os.getenv('EMAIL'),
                    os.getenv('PASSWORD'),
                    captchaElement = self.captchaImage,
                    captchaField = self.captchaField,
                    captchaReader = self.captchaReader
                    ),
                PauseBotAction(seconds = 2),
                ButtonPressAction(self.submitButton),
                PauseBotAction(seconds = 3)
            ])
    
    def _createRoutine(self):
        routine = BotRoutine(
            [
                VisitPageAction(self.driver, self.home_page_url),
                PauseBotAction(seconds = 5),
                RepeatAction(self._LogInSubRoutine(), checkCallback = self.isInAuth),
                VisitPageAction(self.driver,self.target_page_url),
                PauseBotAction(seconds = 4),
                ButtonPressAction(self.comanda),
                PauseBotAction(seconds = 4),
                WriteCommentAction(self.comment,self.commentField,self.submitComment),
                PauseBotAction(seconds = 4)
            ]
        )

        return routine
    
    def start(self):
        self.routine.startAction()
    
    def close(self):
        self.driver.quit()
    
    def isInAuth(self):
        return self.driver.current_url == self.auth_url