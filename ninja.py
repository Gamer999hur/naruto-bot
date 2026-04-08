import random
import json
import asyncio

class Ninja:
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.chakra = 500
        self.jutsus = []
        self.level = 1
        self.xp = 0
    
    def to_dict(self, user_id: str):
        return {
            user_id: {
                "name": self.name,
                "hp": self.hp,
                "chakra": self.chakra,
                "jutsus": self.jutsus,
                "level": self.level,
                "xp": self.xp
            }
        }