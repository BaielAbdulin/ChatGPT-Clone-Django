import os
from dotenv import load_dotenv
from openai import OpenAI

# Get ChatGPT's answer from OpenAI API and return it
def chatgpt_answer(m, q):

    # Get the API key from the .enc=v file
    load_dotenv(os.path.join('/home/ika16/chatgpt', '.env'))
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # Define Model and Gather all message in a correctly formatted Array
    model = "gpt-3.5-turbo"
    # Default System Message
    messages =[{"role": "system", "content": "You are a helpful assistant. You respond completely in HTML format"}]
    for message in m:
        messages.append({"role": "user", "content": message.question})
        messages.append({"role": "assistant", "content": message.answer})
    messages.append({"role": "user", "content": q})

    completion = client.chat.completions.create(
        model = model,
        messages = messages,
    )

    return completion.choices[0].message.content