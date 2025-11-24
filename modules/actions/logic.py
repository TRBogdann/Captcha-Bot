from .action import AbstractBotAction
from .action import BotAction
from collections.abc import Callable

# Repeats the subroutine while the checkCallback returns true
class RepeatAction(AbstractBotAction):
    def __init__(self,action: BotAction, checkCallback: Callable[[],bool]):
        self.action = action
        self.checkCallback = checkCallback
    
    def startAction(self):
        if self.checkCallback():
            self.action.startAction()
            self.startAction()
        else:
            super().startAction()
            


class ConditionalAction(AbstractBotAction):
    def __init__(self,onTrueAction: BotAction,onFalseAction: BotAction, checkCallback: Callable[[],bool]):
        self.onTrueAction = onTrueAction
        self.onFalseAction = onFalseAction
        self.checkCallback = checkCallback
    
    def startAction(self):
        if self.checkCallback():
            if self.onTrueAction:
                self.onTrueAction.startAction()
        else:
            if self.onFalseAction:
                self.onFalseAction.startAction()

        super().startAction()