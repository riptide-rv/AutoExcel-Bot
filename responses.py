from openai import OpenAI
import os
import requests
import dotenv

url = "http://localhost:8000/openai"
url_row = "http://localhost:8000/addrow"

dotenv.load_dotenv()
apik = os.environ.get('OPENAI_API_KEY')


client = OpenAI(api_key=apik)


def handle_request(message) -> str:
    a=""
    b=""
    print(message.author.roles)
    print([r.name for r in message.author.roles])
    if message.content.startswith("context")and 'Manager' in [r.name for r in message.author.roles]:
        a = message.content[7:]
        
        os.environ['A'] = a
        return f"context changed to {a}"
    
    if message.content.startswith("sheet")and 'Manager' in [r.name for r in message.author.roles] :
        c = message.content[5:]
        os.environ['C'] = c
        return f"sheet changed to  {c}"

    if message.content.startswith("columns")and 'Manager' in [r.name for r in message.author.roles] :
        b = message.content[7:]
        os.environ['B'] = b
        return f"columns changed to  {b}"
    
    if message.content.startswith("sheet")and 'Manager' in [r.name for r in message.author.roles] :
        b = message.content[5:]
        b.trim()
        os.environ['C'] = b
        return f"columns changed to {b}"
    p_message = message.content.lower()
    data = {
    "context": os.environ.get('A'),
    "columns": os.environ.get('B'),
    "data": p_message
}
    print(data)
    
    print(os.environ.get('A'))
    print(os.environ.get('B'))
    
    response = requests.post(url, json=data)
    print(response)
    print(response.json())
    response_data = response.json()
    print(response)
    row_data= requests.post(url_row+f"/{os.environ.get('C')}", json=response_data)
    print(row_data)
    
    return   format_message(row_data.json())


def format_message(data):
    formatted_message = "A new row was added:\n"
    for key, value in data.items():
        formatted_message += f"{key.capitalize()} - {value}\n"
    return formatted_message.rstrip('\n')