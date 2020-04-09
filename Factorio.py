import collections

Recipes = {"Automation Science Pack":["Iron Gear Wheel", 1, "Copper Plate", 1],
           "Iron Gear Wheel":["Iron Plate", 2],
           "Iron Plate":["Iron Ore", 1],
           "Copper Plate":["Copper Ore", 1],
           "Iron Ore": 0,
           "Copper Ore":0
           }

#Solution from math: Need 20 Iron Ore and 10 Copper Ore to make 10 Science Packs


def Calculate_ores(qty, ingredients):
    for q in qty:
        for i in qty[q]:
            if ingredients in i:
                return q
    return none

def Calculate(Recipes, qty):
    for key, value in Recipes.items():
        for v in value:
            if qty in v:
                return key
    return None

print(Calculate(1, "Iron Ore"))
