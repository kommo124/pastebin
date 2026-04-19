from fastapi import FastApi
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastApi()

origins = [
    "http://localhost",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class DataForm(BaseModel):
    text str,
    tag str,


async def init_db():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pasteTable (
        text TEXT NOT NULL,
        tag TEXT NOT NULL
    )
''')

conn.commit()

conn.close

@app.post("/submit")
async def submit_form(data: DataForm)
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO pasteTable (text, tag)
    VALUES (?, ?)
    '''), (data.text, data.tag)

    conn.commit()
    conn.close()
