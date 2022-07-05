from reactorItem import BaseReactorItem
from config import OFFSET_X, OFFSET_Y
from neutronreflector import NeutronReflectorItem


class FuelRodItem(BaseReactorItem):

    def __init__(self, durability, rods, e ,h):
        super().__init__(durability)

        self.rods = rods
        self.energyMulti = e
        self.heatMulti = h
        self.pulses = 1 if rods == 1 else 2 if rods == 2 else 3

    def getRods(self):
        return self.rods

    def reactorTickPre(self, reactor, x, y):
        return super().reactorTickPre(reactor, x, y)

    
    def reactorTickPost(self, reactor, x, y):
        
        pulses = self.pulses

        adjacent = [None for i in range(4)]

        for i in range(4):
            adjacent[i] = reactor.reactor[x + OFFSET_X[i]][y + OFFSET_Y[i]]

            if isinstance(adjacent[i], NeutronReflectorItem):
                pulses += 1
        

        reactor.energyOutput += pulses * self.energyMulti
        reactor.distributeHeat(adjacent)
        self.damageItem(1)
        
            



