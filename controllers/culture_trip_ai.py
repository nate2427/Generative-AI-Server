from flask import jsonify
from ai_services.culture_trip_ai import query_agent


def get_all_messages_test():
    # For now, we'll just return a test message.
    # Later, you can replace this with actual logic.
    return jsonify({"message": "This is a test message from culture_trip_ai!"})


def query_ai_agent(query_string):
    response = query_agent(query_string)
    return response
