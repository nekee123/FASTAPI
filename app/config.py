import os
from dotenv import load_dotenv
from neomodel import config

# load env
load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI", "neo4j+s://f16c6d3b.databases.neo4j.io")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# neomodel expects bolt://user:pass@host:port
config.DATABASE_URL = f"{NEO4J_URI.replace('bolt://','bolt://'+NEO4J_USER+':'+NEO4J_PASSWORD+'@')}"
