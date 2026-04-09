import random
import json
import asyncio

clas = ["uchiha", "uzumaki", "hyuuga", "aburame", "inuzuka"]

class Ninja:
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.chakra = 500
        self.jutsus = []
        self.level = 1
        self.xp = 0
        self.cla = random.choice(clas)

    
    def to_dict(self):
        return {
                "name": self.name,
                "cla": self.cla,
                "hp": self.hp,
                "chakra": self.chakra,
                "jutsus": self.jutsus,
                "level": self.level,
                "xp": self.xp}