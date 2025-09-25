from .models import User, Post
from typing import List, Optional
from datetime import datetime

# ===== USER CRUD =====

def create_user(data) -> User:
    return User(username=data.username, name=data.name, bio=data.bio).save()

def get_user(username: str) -> Optional[User]:
    return User.nodes.get_or_none(username=username)

def update_user(username: str, data) -> Optional[User]:
    user = User.nodes.get_or_none(username=username)
    if not user:
        return None
    if data.name:
        user.name = data.name
    if data.bio:
        user.bio = data.bio
    user.save()
    return user

def delete_user(username: str) -> bool:
    user = User.nodes.get_or_none(username=username)
    if not user:
        return False
    user.delete()
    return True

def list_users(limit: int = 25) -> List[User]:
    return list(User.nodes.all())[:limit]


# ===== POST CRUD =====

def create_post(username: str, content: str) -> Optional[Post]:
    user = User.nodes.get_or_none(username=username)
    if not user:
        return None
    post = Post(content=content, created_at=datetime.utcnow()).save()
    user.posts.connect(post)
    return post

def get_post(uid: str) -> Optional[Post]:
    return Post.nodes.get_or_none(uid=uid)

def update_post(uid: str, content: Optional[str]) -> Optional[Post]:
    post = Post.nodes.get_or_none(uid=uid)
    if not post:
        return None
    if content:
        post.content = content
    post.save()
    return post

def delete_post(uid: str) -> bool:
    post = Post.nodes.get_or_none(uid=uid)
    if not post:
        return False
    post.delete()
    return True

def list_posts(limit: int = 25) -> List[Post]:
    return list(Post.nodes.order_by("-created_at"))[:limit]
