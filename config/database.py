import os
import os.path
from multiprocessing import connection

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

ATLAS_URI = os.getenv('ATLAS_URI')

connection_string=ATLAS_URI

print(connection_string)
client = MongoClient(connection_string)

db = client.todo_app

collection_name = db["todos_app"]
