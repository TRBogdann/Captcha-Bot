from bot2 import TestCaptchaBot


if __name__ == '__main__':
    captchaBot = TestCaptchaBot('captcha_model.keras','vocabulary.txt')
    captchaBot.start()
    captchaBot.close()