class Planner:

    def create_plan(self, message, context):

        plan = {
            "message": message,
            "context": context,
            "tool": "default"
        }

        if "image" in message.lower():
            plan["tool"] = "image"

        elif "video" in message.lower():
            plan["tool"] = "video"

        elif "audio" in message.lower():
            plan["tool"] = "audio"

        return plan
