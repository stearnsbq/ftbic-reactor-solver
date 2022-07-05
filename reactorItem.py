
from abc import ABC, abstractmethod


class BaseReactorItem(ABC):
    
    def __init__(self, durability):
        self.durability = durability
        self.damageTaken = 0


    def isCoolant(self):
        return False;

    def isHeatAcceptor(self):
        return False

    def getRods(self):
        return 0
    
    def keepSimulationRunning(self):
        return False

    def isBroken(self):
        return self.damageTaken > 0 and self.damageTaken >= self.durability

    def relativeDamage(self):
        return self.damageTaken / self.durability

    def damageItem(self, damage):

        if(damage != 0):

            extra = 0
            newDamage = self.damageTaken
            newDamage += damage

            if(newDamage > self.durability):
                extra = self.durability - newDamage + 1
                newDamage = self.durability
            elif(newDamage < 0):
                extra = newDamage
                newDamage = 0
            
            self.damageTaken = newDamage

            return extra

        return damage
    
    @abstractmethod
    def reactorTickPre(self, reactor, x, y):
        pass

    @abstractmethod
    def reactorTickPost(self, reactor, x, y):
        pass
