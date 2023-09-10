from mongoengine import Document, StringField, ListField, EmbeddedDocument, EmbeddedDocumentField, DateTimeField
from datetime import datetime


class Message(EmbeddedDocument):
    role = StringField(required=True, choices=["human", "assistant"])
    content = StringField(required=True)
    time = DateTimeField(default=datetime.utcnow)


class Conversation(EmbeddedDocument):
    conversation_id = StringField(required=True)
    messages = ListField(EmbeddedDocumentField(Message))


class User(Document):
    username = StringField(required=True, unique=True)
    conversations = ListField(EmbeddedDocumentField(Conversation))

    meta = {
        'collection': 'users',  # specify the collection name
        'indexes': ['username']
    }
