from plating import ReactorPlatingItem
from reactor import Reactor
from fuelrod import FuelRodItem
from heatexchanger import HeatExchangerItem
from heatvent import HeatVentItem
from neutronreflector import NeutronReflectorItem
from coolant import CoolantItem
from multiprocessing import Pool
import random





# Coolant 

SMALL_COOLANT_CELL = (10_000,)
MEDIUM_COOLANT_CELL = (30_000,)
LARGE_COOLANT_CELL = (60_000,)
COOLANT_CELLS = [SMALL_COOLANT_CELL, MEDIUM_COOLANT_CELL, LARGE_COOLANT_CELL]

# Fuel Rods
SINGLE_FUEL_ROD = (20_000, 1, 5, 2)
DUAL_FUEL_ROD = (20_000, 2, 10, 4)
QUAD_FUEL_ROD = (20_000, 4, 20, 8)
RODS = [SINGLE_FUEL_ROD, DUAL_FUEL_ROD, QUAD_FUEL_ROD]

# Heat Exchangers
HEAT_EXCHANGER = (2_500, 12, 4)
ADVANCED_HEAT_EXCHANGER = (10_000, 24, 8)
REACTOR_HEAT_EXCHANGER = (5_000, 0, 72)
COMPONENT_HEAT_EXCHANGER = (5_000, 36, 0)
EXCHANGERS = [HEAT_EXCHANGER, ADVANCED_HEAT_EXCHANGER, REACTOR_HEAT_EXCHANGER, COMPONENT_HEAT_EXCHANGER]

# Heat Vent
HEAT_VENT = (1_000, 6, 0, 0)
ADVANCED_HEAT_VENT = (1_000, 12, 0, 0)
REACTOR_HEAT_VENT = (1_000, 5, 5, 0)
COMPONENT_HEAT_VENT = (0, 0, 0, 4)
OVERCLOCKED_HEAT_VENT = (1_000, 20, 36, 0)
VENTS = [HEAT_VENT, ADVANCED_HEAT_VENT, REACTOR_HEAT_VENT, COMPONENT_HEAT_VENT, OVERCLOCKED_HEAT_VENT]

# Neutron Reflectors
NEUTRON_REFLECTOR = (30_000,)
THICK_NEUTRON_REFLECTOR = (120_000,)
IRIDIUM_NEUTRON_REFLECTOR = (0,)
REFLECTORS = [NEUTRON_REFLECTOR, THICK_NEUTRON_REFLECTOR, IRIDIUM_NEUTRON_REFLECTOR]

# Plating
REACTOR_PLATING = (1_000, 0.95)
CONTAINMENT_REACTOR_PLATING = (500, 0.90)
HEAT_CAPACITY_REACTOR_PLATING = (1_700, 0.99)
PLATING = [REACTOR_PLATING, CONTAINMENT_REACTOR_PLATING, HEAT_CAPACITY_REACTOR_PLATING]


itemList = ['coolant', 'fuelrod', 'heatexchanger', 'heatvent', 'reflector', 'plating']

def doReactorSim(self, reactor):
    pass




def main():

    run = True

    best = None

    for i in range(1):
        reactors = [generateRandomReactor() for i in range(16)]

        print(reactors)


    
    





# 'coolant', 'fuelrod', 'heatexchanger', 'heatvent', 'reflector', 'plating'

def generateRandomReactor():
    reactor = Reactor()

    for x in range(reactor.WIDTH):
        for y in range(reactor.HEIGHT):
            itemChoice = random.choice(itemList)
            
            item = None
            if itemChoice == 'coolant':
                item = CoolantItem(*random.choice(COOLANT_CELLS))
            elif itemChoice == 'fuelRod':
                item = FuelRodItem(*random.choice(RODS))
            elif itemChoice == 'heatexchanger':
                item = HeatExchangerItem(*random.choice(EXCHANGERS))
            elif itemChoice == 'heatvent':
                item = HeatVentItem(*random.choice(VENTS))
            elif itemChoice == 'reflector':
                item = NeutronReflectorItem(*random.choice(REFLECTORS))
            elif itemChoice == 'plating':
                item = ReactorPlatingItem(*random.choice(PLATING))


            reactor.reactor[y][x] = item
















if __name__ == '__main__':
    main()
