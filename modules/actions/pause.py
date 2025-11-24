import time
from .action import AbstractBotAction

class PauseBotAction(AbstractBotAction):
    def __init__(self,seconds):
        self.seconds = seconds

    def startAction(self):
        time.sleep(self.seconds)
        super().startAction()