from openai import OpenAI
client = OpenAI()


def chat_gpt(messages):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[messages])
    return response.choices[0].message.content