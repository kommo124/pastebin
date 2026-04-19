from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class DataForm(BaseModel):
    text: str
    tag: str


def init_db():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pasteTable (
        text TEXT NOT NULL,
        tag TEXT NOT NULL
    )
''')

    conn.commit()

    conn.close()

init_db()

@app.post("/submit")
async def submit_form(data: DataForm):
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO pasteTable (text, tag)
        VALUES (?, ?)
        ''', (data.text, data.tag))

    cursor.execute("SELECT * FROM pasteTable")
    conn.commit()
    conn.close()


@app.get('/data')
async def getData():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pasteTable")
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return [{"text": r[0], "tag": r[1]} for r in rows]