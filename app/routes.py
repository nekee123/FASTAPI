from fastapi import APIRouter, HTTPException
from . import controllers, schemas

router = APIRouter(prefix="/api")

# Users
@router.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate):
    u = controllers.create_user(user)
    return schemas.UserOut(**u.__properties__)

@router.get("/users/{username}", response_model=schemas.UserOut)
def get_user(username: str):
    u = controllers.get_user(username)
    if not u:
        raise HTTPException(404, "User not found")
    return schemas.UserOut(**u.__properties__)

@router.patch("/users/{username}", response_model=schemas.UserOut)
def update_user(username: str, payload: schemas.UserUpdate):
    u = controllers.update_user(username, payload)
    if not u:
        raise HTTPException(404, "User not found")
    return schemas.UserOut(**u.__properties__)

@router.delete("/users/{username}")
def delete_user(username: str):
    ok = controllers.delete_user(username)
    if not ok:
        raise HTTPException(404, "User not found")
    return {"deleted": True}

@router.get("/users", response_model=list[schemas.UserOut])
def list_users(limit: int = 25):
    users = controllers.list_users(limit)
    return [schemas.UserOut(**u.__properties__) for u in users]


# Posts
@router.post("/posts", response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate):
    p = controllers.create_post(post.username, post.content)
    if not p:
        raise HTTPException(404, "User not found")
    return schemas.PostOut(uid=p.uid, content=p.content, created_at=p.created_at, author=post.username)

@router.get("/posts/{uid}", response_model=schemas.PostOut)
def get_post(uid: str):
    p = controllers.get_post(uid)
    if not p:
        raise HTTPException(404, "Post not found")
    author = p.posted_by.single().username if hasattr(p, "posted_by") else "unknown"
    return schemas.PostOut(uid=p.uid, content=p.content, created_at=p.created_at, author=author)

@router.patch("/posts/{uid}", response_model=schemas.PostOut)
def update_post(uid: str, payload: schemas.PostUpdate):
    p = controllers.update_post(uid, payload.content)
    if not p:
        raise HTTPException(404, "Post not found")
    author = p.posted_by.single().username if hasattr(p, "posted_by") else "unknown"
    return schemas.PostOut(uid=p.uid, content=p.content, created_at=p.created_at, author=author)

@router.delete("/posts/{uid}")
def delete_post(uid: str):
    ok = controllers.delete_post(uid)
    if not ok:
        raise HTTPException(404, "Post not found")
    return {"deleted": True}

@router.get("/posts", response_model=list[schemas.PostOut])
def list_posts(limit: int = 25):
    posts = controllers.list_posts(limit)
    out = []
    for p in posts:
        author = p.posted_by.single().username if hasattr(p, "posted_by") else "unknown"
        out.append(schemas.PostOut(uid=p.uid, content=p.content, created_at=p.created_at, author=author))
    return out
