from g4f.client import Client
from md_convert import convert
from cfg import *

def get_responce(responce_data):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Перепиши кратко:\n{responce_data}"}],

    )
    return response.choices[0].message.content

#print(get_responce(convert(d_02, d02f02)))
