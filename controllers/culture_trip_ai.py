from flask import jsonify


def get_all_messages_test():
    # For now, we'll just return a test message.
    # Later, you can replace this with actual logic.
    return jsonify({"message": "This is a test message from culture_trip_ai!"})
