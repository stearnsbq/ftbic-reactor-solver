from reactorItem import BaseReactorItem
class ReactorPlatingItem(BaseReactorItem):

    def __init__(self, h, e):
        super().__init__(0)
        self.maxHeatBonus = h
        self.explosionRadius = e

    

    def reactorTickPre(self, reactor, x, y):
        reactor.maxHeat += self.maxHeatBonus
        