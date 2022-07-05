from reactorItem import BaseReactorItem
from config import OFFSET_X, OFFSET_Y


class NeutronReflectorItem(BaseReactorItem):

    def __init__(self, durability):
        super().__init__(durability)



    def reactorTickPost(self, reactor, x, y):
        if(self.durability <= 0):
            return
        
        for i in range(4):
            item = reactor.reactor[x + OFFSET_X[i]][y + OFFSET_Y[i]]

            if isinstance(item, BaseReactorItem):
                item.damageItem(item.getRods())
        

  
