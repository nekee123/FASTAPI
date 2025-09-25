from fastapi import FastAPI
from .routes import router
from . import config  # initializes neomodel connection

app = FastAPI(title="Social Media Backend (FastAPI + Neo4j)")

# Include your API routes
app.include_router(router)

# 👇 Add this root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Social Media Backend (FastAPI + Neo4j)!"}
