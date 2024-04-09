import os
import openai
from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from amigo_response import get_chat_response

app = FastAPI()

# Load environment variables from .env file
load_dotenv()


class Message(BaseModel):
    input_string: str

# Access the API key
api_key = os.getenv('OPEN_AI_API_KEY')

# Check if the API key is empty or not found
if not api_key:
    print("Error: API key not found in environment variables.")
    exit()

# Instantiate the OpenAI client
client = openai.OpenAI(api_key=api_key)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send_message/")
async def send_message(message: Message):
    # response = get_chat_response(client, input_string)
    # return {"response": response}
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Your AI friend"}, {"role": "user", "content": message.input_string}]
    )
    return {"response": response.choices[0].message.content}


# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="127.0.0.1", port=5001)
