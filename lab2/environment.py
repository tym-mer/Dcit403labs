import random

class DisasterEnvironment:
    def get_conditions(self):
        return {
            "temperature": random.randint(20, 100),
            "smoke": random.randint(0, 100),
            "damage": random.randint(0, 100)
        }
