from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import openai


app = FastAPI()
key = os.environ.get("openai_key")
openai.api_key = key

origins = [
    "http://localhost",
    "http://127.0.0.1:8000/"
    "http://127.0.0.1:5500/",
    
]

# Allow requests from all origins (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    text: str

@app.post('/process', response_model=dict)
async def process_text(user_input: UserInput):
    processed_input = user_input.text.lower()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="convert input into Gen Z slang. " + processed_input,
        max_tokens=30,
        temperature=0
    )

    return JSONResponse(content={'result': response['choices'][0]["text"]})
