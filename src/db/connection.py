from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()

db_path = os.getenv("db_path", "data/db/limiter.db")

def get_connection():
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except:
        print("connection failed")

#END WITH TUSHAR