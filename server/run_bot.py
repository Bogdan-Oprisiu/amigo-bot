import os
import openai
from dotenv import load_dotenv

from amigo_response import get_chat_response

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv('OPEN_AI_API_KEY')

# Check if the API key is empty or not found
if not api_key:
    print("Error: API key not found in api_key.txt or the file is empty.")


def main():
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        return

    # Instantiate the OpenAI client
    client = openai.OpenAI(api_key=api_key)

    print(
        "Welcome to the Amigo bot! I'm your friendly and cheerful companion."
        " Let's chat about anything! Type 'Goodbye' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'goodbye':
            print("Goodbye! May the force be with you!")
            break

        else:
            response = get_chat_response(client, user_input)

            if response:
                print("Amigo: " + response)


if __name__ == "__main__":
    main()
