import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime
import json


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")


client = Groq(api_key=api_key)


def get_response(messages):
    try:

        stream = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",  # Adjust to your model
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=True,
        )

        response_content = ""
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                response_content += chunk.choices[0].delta.content

        return response_content
    except Exception as e:
        return f"Error: {str(e)}"


def summarize_chat(history):
    summary_prompt = "Summarize the following chat:\n"
    for message in history:
        summary_prompt += f"{message['role']}: {message['content']}\n"

    return get_response(
        [
            {
                "role": "system",
                "content": "You are an assistant that summarizes conversations.",
            },
            {"role": "user", "content": summary_prompt},
        ]
    )


def save_summary(summary):
    try:
        with open("chat_summary.json", "w") as f:
            json.dump({"summary": summary}, f)
    except Exception as e:
        print(f"Error saving summary: {str(e)}")


def load_summary():
    try:
        if os.path.exists("chat_summary.json"):
            with open("chat_summary.json", "r") as f:
                data = json.load(f)
                return data.get("summary", "")
        return ""
    except Exception as e:
        print(f"Error loading summary: {str(e)}")
        return ""


def chat():
    print("Welcome to your personal chatbot! (Type 'exit' to quit)")

    # Load the previous summary if available
    previous_summary = load_summary()
    if previous_summary:
        print(f"Previous chat summary:\n{previous_summary}")

    history = []

    if previous_summary:
        history.append(
            {"role": "system", "content": f"Previous chat summary: {previous_summary}"}
        )

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye! I'll miss you! ❤️")

            summary = summarize_chat(history)
            print(f"Chat Summary:\n{summary}")
            save_summary(summary)
            break

        if not user_input.strip():
            print("Chatbot: Please enter a message.")
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        history.append({"role": "user", "content": f"{timestamp} - {user_input}"})
        response = get_response(
            [
                {
                    "role": "system",
                    "content": "You are a supportive and affectionate girlfriend chatbot.",
                },
                {"role": "user", "content": user_input},
            ]
        )

        history.append({"role": "assistant", "content": f"{timestamp} - {response}"})

        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()
