import openai


def get_chat_response(client, user_input):
    try:
        prompt_messages = [
            {"role": "user", "content": user_input},
            {"role": "system", "content": "Hey there! It's your best buddy Amigo. "}
        ]

        # Create completion
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt_messages,
            max_tokens=100,  # Adjust max_tokens to control response length
            temperature=0.7,  # Adjust temperature for creativity in responses
        )

        return completion.choices[0].message.content

    except openai.OpenAIError as e:
        print("OpenAI API Error:", e)
        return None

    except Exception as e:
        print("An unexpected error occurred:", e)
        return None
