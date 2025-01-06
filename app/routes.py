from flask import Blueprint, request, jsonify, render_template
from app.gpt2_service import GPT2Service
from app.memory import Memory

chat = Blueprint('chat', __name__)

# Initialize GPT-2 service and memory
gpt2_service = GPT2Service()
memory = Memory()

@chat.route('/')
def index():
    return render_template('chat.html')

@chat.route('/chat', methods=['POST'])
def chat_route():
    user_input = request.json.get('message')
    conversation_history = memory.get_memory()
    response = gpt2_service.generate_response(user_input, conversation_history)
    memory.update_memory(user_input, response)
    return jsonify({'response': response})

import random

@chat.route('/plan_trip', methods=['POST'])
def plan_trip_route():
    # Extract trip details from the request
    data = request.json
    departure_date = data.get('departure_date')
    return_date = data.get('return_date')
    hotel_preference = data.get('hotel_preference')
    activities = data.get('activities')

    # Structured prompt for trip planning
    prompt = (
        f"Plan a trip itinerary with the following details:\n"
        f"- Departure Date: {departure_date}\n"
        f"- Return Date: {return_date}\n"
        f"- Hotel Preference: {hotel_preference}\n"
        f"- Activities: {activities}\n\n"
        "Provide a daily itinerary, suggesting hotels and flights."
    )

    # Generate a response from the GPT-2 model
    response = gpt2_service.generate_response(prompt, "")

    # Add mock links to hotel and flights
    hotel_links = [
        "https://www.booking.com/hotel/demo1",
        "https://www.booking.com/hotel/demo2",
        "https://www.airbnb.com/rooms/demo1"
    ]
    flight_links = [
        "https://www.skyscanner.com/flights/demo1",
        "https://www.expedia.com/Flights-Demo"
    ]

    # Append mock links for hotels and flights in the response
    response += "\n\nSuggested Hotels:\n"
    for link in hotel_links:
        response += f"{link}\n"

    response += "\nSuggested Flights:\n"
    for link in flight_links:
        response += f"{link}\n"

    return jsonify({'response': response})
