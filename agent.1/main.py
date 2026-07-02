from brain import Brain
from planner import Planner
from memory import Memory
from tools import ToolManager


class AstraMindAgent:

    def __init__(self):
        self.brain = Brain()
        self.planner = Planner()
        self.memory = Memory()
        self.tools = ToolManager()

    def process(self, message):

        context = self.memory.load_context()

        plan = self.planner.create_plan(
            message,
            context
        )

        tool_result = self.tools.execute(plan)

        response = self.brain.generate_response(
            message,
            tool_result
        )

        self.memory.save_context(
            message,
            response
        )

        return response


if __name__ == "__main__":
    agent = AstraMindAgent()

    while True:

        user = input("You: ")

        if user.lower() == "exit":
            break

        reply = agent.process(user)

        print("AstraMind:", reply)
