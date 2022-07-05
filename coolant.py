from reactorItem import BaseReactorItem

class CoolantItem(BaseReactorItem):

    def __init__(self, durability):
        super().__init__(durability)


    def isHeatAcceptor(self):
        return self.durability > 0