from transformers import pipeline

class GPT2Service:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")

    def generate_response(self, user_input, conversation_history):
        # Limit conversation history to the last 50 tokens (or characters) to manage length
        if len(conversation_history) > 50:
            conversation_history = conversation_history[-50:]

        # Create a prompt with user input and limited conversation history
        prompt = f"{conversation_history}\nUser: {user_input}\nAI:"
        
        # Generate response with max_new_tokens to limit output length
        response = self.generator(prompt, max_new_tokens=50, num_return_sequences=1)[0]['generated_text']
        
        # Extract the chatbot's response and trim it down to avoid overly verbose answers
        response_text = response[len(prompt):].strip().split('\n')[0]
        
        return response_text
