class Memory:

    def __init__(self):
        self.history = []

    def load_context(self):
        return self.history

    def save_context(self, message, response):
        self.history.append({
            "user": message,
            "assistant": response
        })

    def clear(self):
        self.history = []
