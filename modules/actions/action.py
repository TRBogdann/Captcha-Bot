from __future__ import annotations
from abc import ABC, abstractmethod

class BotAction(ABC):
    @abstractmethod
    def setNextAction(self,action: BotAction):
        pass

    def  startAction(self,):
        pass 


class AbstractBotAction(BotAction):
    _next_action: BotAction = None

    def setNextAction(self, action: BotAction):
            self._next_action = action

    def startAction(self):
        if self._next_action:
             self._next_action.startAction()