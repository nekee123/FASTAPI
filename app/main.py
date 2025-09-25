from fastapi import FastAPI
from .routes import router
from . import config  # initializes neomodel connection
from neomodel import db

app = FastAPI(title="Social Media Backend (FastAPI + Neo4j)")

# Include your API routes
app.include_router(router)

# 👇 Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Social Media Backend (FastAPI + Neo4j)!"}

# 👇 Check Neo4j connection on startup
@app.on_event("startup")
def startup_db_check():
    try:
        db.cypher_query("RETURN 1")
        print("[INFO] ✅ Connected to Neo4j successfully")
    except Exception as e:
        print("[ERROR] ❌ Could not connect to Neo4j")
        print(f"Details: {e}")
