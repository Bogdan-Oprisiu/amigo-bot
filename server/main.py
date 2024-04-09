import os

import openai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from amigo_response import get_chat_response

app = FastAPI()

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv('OPEN_AI_API_KEY')

# Check if the API key is empty or not found
if not api_key:
    print("Error: API key not found in api_key.txt or the file is empty.")

client = openai.OpenAI(api_key=api_key)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send_message/")
async def send_message(input_string: str):
    response = get_chat_response(client, input_string)
    return {"response": response}
