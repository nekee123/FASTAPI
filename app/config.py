import os
from dotenv import load_dotenv
from neomodel import config

# Load environment variables from .env
load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI", "neo4j+s://f16c6d3b.databases.neo4j.io")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# Convert neo4j+s:// -> bolt+s:// for neomodel
if NEO4J_URI.startswith("neo4j+s://"):
    uri_clean = NEO4J_URI.replace("neo4j+s://", "bolt+s://")
elif NEO4J_URI.startswith("neo4j://"):
    uri_clean = NEO4J_URI.replace("neo4j://", "bolt://")
else:
    uri_clean = NEO4J_URI

# neomodel expects: bolt+s://user:password@host:7687
host = uri_clean.split("://")[1]  # f16c6d3b.databases.neo4j.io
config.DATABASE_URL = f"bolt+s://{NEO4J_USER}:{NEO4J_PASSWORD}@{host}:7687"

print("✅ Connected to Neo4j Aura via:", config.DATABASE_URL)
