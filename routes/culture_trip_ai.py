from flask import jsonify
from . import routes
from controllers import culture_trip_ai as culture_trip_ai_controller


@routes.route('/culture-trip-ai/get-all-messages-test', methods=['GET'])
def get_all_messages_test():
    return culture_trip_ai_controller.get_all_messages_test()
