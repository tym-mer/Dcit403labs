from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio
from environment import DisasterEnvironment

class SensorBehaviour(CyclicBehaviour):
    async def run(self):
        conditions = self.agent.environment.get_conditions()

        damage = conditions["damage"]
        if damage <= 30:
            severity = "Minor"
        elif damage <= 70:
            severity = "Moderate"
        else:
            severity = "Severe"

        print("---- Sensor Reading ----")
        print(f"Temperature: {conditions['temperature']}°C")
        print(f"Smoke Level: {conditions['smoke']}")
        print(f"Damage Level: {damage} ({severity})")
        print("------------------------\n")

        await asyncio.sleep(5)


class SensorAgent(Agent):
    async def setup(self):
        print("SensorAgent started and monitoring environment...")
        self.environment = DisasterEnvironment()
        self.add_behaviour(SensorBehaviour())


async def main():
    agent = SensorAgent("sensor@localhost", "password123")
    await agent.start(auto_register=True)
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
