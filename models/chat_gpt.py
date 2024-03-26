import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)


def invoke_chat_gpt(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[messages]
    )
    return response.choices[0].message.content
