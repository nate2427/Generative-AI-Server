from models.culture_trip_ai import User, Message, Conversation
from dotenv import load_dotenv
import os
from mongoengine import connect, DoesNotExist
from datetime import datetime
import sys
from bson import ObjectId
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
load_dotenv()


CULTURE_TRIP_AI_DB_PWD = os.getenv("CULTURE_TRIP_AI_DB_PWD")
CULTURE_TRIP_AI_DB_USER = os.getenv("CULTURE_TRIP_AI_DB_USER")
CULTURE_TRIP_AI_DB_URL = os.getenv("CULTURE_TRIP_AI_DB_URL")

uri = f"mongodb+srv://{CULTURE_TRIP_AI_DB_USER}:{CULTURE_TRIP_AI_DB_PWD}@{CULTURE_TRIP_AI_DB_URL}"

client = connect(db="culture_trip_db", host=uri, port=27017)


class UserService:

    @staticmethod
    def create_user(username):
        user = User(username=username)
        user.save()
        return user

    @staticmethod
    def start_conversation(username):
        user = User.objects(username=username).first()
        if not user:
            raise DoesNotExist("User not found")

        conversation = Conversation(
            conversation_id=str(ObjectId()), messages=[])
        user.conversations.append(conversation)
        user.save()
        return conversation.conversation_id

    @staticmethod
    def insert_message(username, conversation_id, role, content):
        user = User.objects(username=username).first()
        if not user:
            raise DoesNotExist("User not found")

        message = Message(role=role, content=content, time=datetime.utcnow())
        for conversation in user.conversations:
            if conversation.conversation_id == conversation_id:
                conversation.messages.append(message)
                user.save()
                return message

        raise ValueError("Conversation not found")

    @staticmethod
    def get_messages(username, conversation_id):
        user = User.objects(username=username).first()
        if not user:
            raise DoesNotExist("User not found")

        for conversation in user.conversations:
            if conversation.conversation_id == conversation_id:
                return conversation.messages

        return []

    @staticmethod
    def get_all_conversations(username):
        user = User.objects(username=username).first()
        if not user:
            raise DoesNotExist("User not found")

        return user.conversations


def test_user_service_operations():
    # Create a user
    # user = UserService.create_user("john_doe")
    # print(f"Created User: {user.username}")

    # Start a new conversation for the user
    conversation_id = UserService.start_conversation("john_doe")
    print(f"Started Conversation with ID: {conversation_id}")

    # Insert a message into the conversation
    message = UserService.insert_message(
        "john_doe", conversation_id, "human", "Hello, AI!")
    print(
        f"Inserted Message: {message.content} by {message.role} at {message.time}")

    # insert a bot message
    message = UserService.insert_message(
        "john_doe", conversation_id, "assistant", "Hello, human!")
    print(
        f"Inserted Message: {message.content} by {message.role} at {message.time}"
    )

    # Retrieve messages from the conversation
    messages = UserService.get_messages("john_doe", conversation_id)
    print("Messages in the Conversation:")
    for msg in messages:
        print(f"{msg.role}: {msg.content} at {msg.time}")

    # Retrieve all conversations for the user
    conversations = UserService.get_all_conversations("john_doe")
    print(f"Total Conversations for john_doe: {len(conversations)}")

    # Note: For the sake of this test function, we're not implementing delete operations.
    # If you want to test delete or update operations, similar steps can be added.
