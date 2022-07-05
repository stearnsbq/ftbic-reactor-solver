from reactorItem import BaseReactorItem
from config import OFFSET_X, OFFSET_Y
class HeatVentItem(BaseReactorItem):
    
    def __init__(self, durability, selfCooling, reactorCooling, componentCooling):
        super().__init__(durability)

        self.selfCooling = selfCooling
        self.reactorCooling = reactorCooling
        self.componentCooling = componentCooling

    
    def isHeatAcceptor(self):
        return self.durability > 0

    
    def reactorTickPre(self, reactor, x, y):
        if self.reactorCooling > 0:
            reactor.addHeat(-self.reactorCooling)
        

        if self.selfCooling > 0:
            self.damageItem(-self.selfCooling)
        

        if self.componentCooling > 0:

            for i in range(4):
                item = reactor[x + OFFSET_X[i]][y + OFFSET_Y[i]]

                if isinstance(item, BaseReactorItem) and item.isCoolant():
                    item.damageItem(-self.componentCooling)