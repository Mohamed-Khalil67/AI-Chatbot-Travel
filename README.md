# AI Chatbot with GPT-2 and Flask  

## Overview  
This project is a conversational AI chatbot built with Hugging Face's GPT-2 model and Flask framework. It provides intelligent responses while maintaining conversation context and includes a specialized trip planning feature.  

## Features  
- **Conversational AI**: GPT-2 powered text generation with context awareness  
- **Memory System**: Tracks and manages conversation history  
- **Trip Planning**: Generates detailed travel itineraries with hotel and flight suggestions  
- **Web Interface**: Ready for integration with frontend applications via REST API  

## File Structure  
- **routes.py**: Contains Flask API endpoints for chat and trip planning  
- **gpt2_service.py**: Handles GPT-2 text generation with response length management  
- **memory.py**: Manages conversation history storage and retrieval  
- **templates/chat.html**: Web interface for the chat functionality  

## Installation  
1. Clone the repository:  
   `git clone https://github.com/yourusername/ai-chatbot.git`  
   `cd ai-chatbot`  

2. Install Python dependencies:  
   `pip install flask transformers torch`  

3. Run the Flask application:  
   `flask run`  

## API Endpoints  

### Chat Interface  
- **GET /**  
  Renders the chat interface webpage.  

- **POST /chat**  
  Processes user messages and returns AI responses.  
  **Request format:**  
  ```json
  {"message": "your message here"}
  ```  

### Trip Planning  
- **POST /plan_trip**  
  Generates a travel itinerary based on user preferences.  
  **Request format:**  
  ```json
  {
    "departure_date": "YYYY-MM-DD",
    "return_date": "YYYY-MM-DD",
    "hotel_preference": "preference",
    "activities": ["activity1", "activity2"]
  }
  ```  

## Configuration  
Adjust the GPT-2 model parameters in **gpt2_service.py** to control response length and quality:  
- `max_new_tokens`: Limits response length  
- `num_return_sequences`: Controls number of generated responses  

## Memory Management  
The conversation history can be cleared by calling:  
`memory.clear_memory()`  

## Requirements  
- Python 3.7 or higher  
- Flask  
- Transformers library (Hugging Face)  
- PyTorch  

## License  
MIT License  

## Contributing  
Contributions are welcome! Please open an issue to discuss major changes before submitting a pull request.
