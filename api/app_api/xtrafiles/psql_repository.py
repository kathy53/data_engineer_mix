# from typing import Optional, Dict
# from app_api.xtrafiles.property import Property
# from app_api.xtrafiles.base_repository import PropertyRepository
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

import os
url = URL.create(
    drivername="postgresql",
    username=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    database=os.getenv("DATABASE")
)

engine = create_engine(url)

try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect to the database: {e}")