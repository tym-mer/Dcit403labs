from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio


class HelloBehaviour(CyclicBehaviour):
    async def run(self):
        print("Hello! Agent is running.")
        await asyncio.sleep(5)

# Define the agent
class HelloAgent(Agent):
    async def setup(self):
        print("Agent started") 
        self.add_behaviour(HelloBehaviour())

async def main():
    agent = HelloAgent("agent1@localhost", "password123")
    try:
        await agent.start(auto_register=True)
        print("Agent running. Press Ctrl+C to stop.")
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, asyncio.CancelledError):
        print("\nStopping agent...")
        await agent.stop()
        print("Agent stopped.")

if __name__ == "__main__":
    asyncio.run(main())
