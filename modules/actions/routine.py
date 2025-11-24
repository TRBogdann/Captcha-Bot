from .action import AbstractBotAction
from .action import BotAction

class BotRoutine(AbstractBotAction):
    def __init__(self,actions: list[BotAction] = []):
        self.actions = actions

        for i in range(len(self.actions)-1):
            self.actions[i].setNextAction(self.actions[i+1])

    def begin(self):
        if len(self.actions) > 0:
            return self.actions[0]
        
        return None
    
    def end(self):
        if len(self.actions) > 0:
            return self.actions[::-1]
    
    def getAction(self, index: int):
        if index >= len(self.actions) or index < 0:
            raise IndexError('[Bot Routine]: Index out of bounds')
        
        return self.actions[index]
    
    def startAction(self):
        if len(self.actions)>0:
            self.begin().startAction()

        super().startAction()