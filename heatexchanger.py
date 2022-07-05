import math
from config import OFFSET_X, OFFSET_Y

from reactorItem import BaseReactorItem

class HeatExchangerItem(BaseReactorItem):

    def __init__(self, durability, adjacentHeatTransfer, coreHeatTransfer):
        super().__init__(durability)

        self.adjacentHeatTransfer = adjacentHeatTransfer
        self.coreHeatTransfer = coreHeatTransfer



    def isHeatAcceptor(self):
        return self.durability > 0


    def reactorTickPre(self, reactor, x, y):
        damage = 0

        if self.adjacentHeatTransfer > 0:

            for i in range(4):
                item = reactor[y + OFFSET_Y[i]][x + OFFSET_X[i]]

                if isinstance(item, BaseReactorItem) and item.isHeatAcceptor():
                    sh = self.relativeDamage() * 100.0
                    rh = item.relativeDamage() * 100.0

                    heat = self._getHeatTransfer(sh, rh, item.durability, self.adjacentHeatTransfer)

                    damage -= heat
                    damage += item.damageItem(heat)
        
        if self.coreHeatTransfer > 0:
            sh = self.relativeDamage() * 100.0
            rh = reactor.heat * 100.0 / reactor.maxHeat

            heat = self._getHeatTransfer(sh, rh, reactor.maxHeat, self.coreHeatTransfer)
            damage -= heat

            reactor.addHeat(heat)

        
        self.damageItem(damage)
    


    def _getHeatTransfer(sh, rh, max, transfer):

        hh = rh + sh / 2.0

        add = min(math.floor(max * hh / 100), transfer)

        if hh < 0.25:
            add = 1
        elif hh < 0.5:
            add = transfer / 8
        elif hh < 0.75: 
            add = transfer / 4
        elif hh < 1.0: 
            add = transfer / 2
        

        frh = math.floor(rh * 10.0) / 10.0
        fsh = math.floor(sh * 10.0) / 10.0

        if frh > fsh:
            add -= 2 * add
        elif frh == fsh:
            add = 0
        


        return add
        
		

    
