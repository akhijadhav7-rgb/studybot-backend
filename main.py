from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"message": "StudyBot is running"}

@app.post("/chat")
def chat(q: str):
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": q}]
    )
    return {"answer": r.choices[0].message.content}
