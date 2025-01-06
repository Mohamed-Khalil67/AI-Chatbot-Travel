class Memory:
    def __init__(self):
        self.conversation_history = []

    def get_memory(self):
        # Combine the stored conversation history
        return "\n".join(self.conversation_history)

    def update_memory(self, user_input, ai_response):
        # Append the latest interaction to the memory
        self.conversation_history.append(f"User: {user_input}")
        self.conversation_history.append(f"AI: {ai_response}")

    def clear_memory(self):
        # Clear the conversation history
        self.conversation_history = []
