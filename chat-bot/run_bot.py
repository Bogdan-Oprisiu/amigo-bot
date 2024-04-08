import os
import openai

# Access the API key from api_key.txt
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

# Check if the API key is empty or not found
if not api_key:
    print("Error: API key not found in api_key.txt or the file is empty.")


def get_chat_response(client, user_input):
    try:
        # Construct the prompt message to always reflect a friendly and cheerful tone
        prompt_messages = [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": "Hey there! I'm your friendly and cheerful companion. "}
        ]

        # Create completion
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt_messages,
        )

        return completion.choices[0].message.content

    except openai.OpenAIError as e:
        print("OpenAI API Error:", e)
        return None

    except Exception as e:
        print("An unexpected error occurred:", e)
        return None


def main():
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        return

    # Instantiate the OpenAI client
    client = openai.OpenAI(api_key=api_key)

    print(
        "Welcome to the Amigo bot! I'm your friendly and cheerful companion."
        " Let's chat about anything! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye! May the force be with you!")
            break

        response = get_chat_response(client, user_input)

        if response:
            print("Amigo: " + response)


if __name__ == "__main__":
    main()
