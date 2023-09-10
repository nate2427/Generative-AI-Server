from flask import jsonify, request
from . import routes
from controllers import culture_trip_ai as culture_trip_ai_controller


@routes.route('/culture-trip-ai/get-all-messages-test', methods=['GET'])
def get_all_messages_test():
    return culture_trip_ai_controller.get_all_messages_test()


@routes.route('/culture-trip-ai/query-ai-agent', methods=['POST'])
def query_ai_agent():
    data = request.get_json()
    message = data['message']
    return jsonify({'message': culture_trip_ai_controller.query_ai_agent(message)})
