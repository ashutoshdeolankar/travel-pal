"""
Travel Pal — Phase 6: database connection.

Reads the connection string from the DATABASE_URL environment
variable (loaded from a local .env file — never commit that file,
it's already in .gitignore). Falls back to a sensible local default
if DATABASE_URL isn't set, but you must still supply your own
Postgres password via .env for that default to work.

Create a file named .env in the project root (same folder as
requirements.txt) with a line like:

    DATABASE_URL=postgresql://postgres:YOUR_PASSWORD_HERE@localhost:5432/travelpal
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/travelpal"
)

engine = create_engine(DATABASE_URL)