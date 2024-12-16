# from typing import Optional, Dict
# from app_api.xtrafiles.property import Property
# from app_api.xtrafiles.base_repository import PropertyRepository
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

import pdb


DATABASE = "properties"
USER = "prooperties_dev"
PASSWORD = "properties_dev"
HOST = "192.168.178.165"
PORT = "5432"



url = URL.create(
    drivername="postgresql",
    username=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DATABASE
)

engine = create_engine(url)

try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Failed to connect to the database: {e}")