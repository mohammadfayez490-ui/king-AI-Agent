class ToolManager:

    def execute(self, plan):

        tool = plan.get("tool", "default")

        if tool == "image":
            return "Image generation tool selected."

        elif tool == "video":
            return "Video generation tool selected."

        elif tool == "audio":
            return "Audio generation tool selected."

        return None
