import math
from reactorItem import BaseReactorItem

class Reactor():
    WIDTH = 9;
    HEIGHT = 6

    def __init__(self) -> None:
        self.reactor = [[None] * self.WIDTH for i in range(self.HEIGHT)]
        self.heat = 0
        self.maxHeat = 0
        self.explosionRadius = 0
        self.energyOutput = 0

    def addHeat(self, h):
        self.heat = max(self.heat + h, 0)

    def distributeHeat(self, adjacentItems, heat):
        pass

    def tick(self):
        stop = False

        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                item = self.reactor[x][y]

                if isinstance(item, BaseReactorItem):
                    item.reactorTickPre(self, x, y)

                    if item.isBroken():
                        self.reactor[x][y] = None


        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                item = self.reactor[x][y]

                if isinstance(item, BaseReactorItem):
                    item.reactorTickPost(self, x, y)

                    if item.isBroken():
                        self.reactor[x][y] = None

        
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                item = self.reactor[x][y]

                if isinstance(item, BaseReactorItem):
                    item.reactorTickPost(self, x, y)

                    if item.isBroken():
                        self.reactor[x][y] = None

        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                item = self.reactor[x][y]

                if isinstance(item, BaseReactorItem):

                    if item.keepSimulationRunning():
                        stop = True
                    elif item.isBroken():
                        self.reactor[x][y] = None
        


        self.heat = max(0, self.heat)

        if self.heat >= self.maxHeat:
            stop = True

        return stop
        


