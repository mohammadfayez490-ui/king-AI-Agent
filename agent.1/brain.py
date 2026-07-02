class Brain:

    def __init__(self):
        self.name = "AstraMind"

    def generate_response(self, message, tool_result):

        if tool_result:
            return tool_result

        return f"I understand your request: {message}"
