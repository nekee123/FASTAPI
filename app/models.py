from neomodel import (
    StructuredNode, StringProperty, DateTimeProperty,
    RelationshipTo, UniqueIdProperty
)
from datetime import datetime

class User(StructuredNode):
    uid = UniqueIdProperty()
    username = StringProperty(unique_index=True, required=True)
    name = StringProperty()
    bio = StringProperty()

    posts = RelationshipTo("Post", "POSTED")


class Post(StructuredNode):
    uid = UniqueIdProperty()
    content = StringProperty(required=True)
    created_at = DateTimeProperty(default=datetime.utcnow)
