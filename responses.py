from openai import OpenAI
import os
import requests
import dotenv

url = "http://localhost:8000/openai"
url_row = "http://localhost:8000/addrow"






def handle_request(message) -> str:
    a=""
    b=""
    print(message.author.roles)
    print([r.name for r in message.author.roles])

    if(message.content=="help"):
        return """`1. Create a new spread sheet. (take care that name of spread sheet has no spaces)\n2. Give editor access to given mail autoexcelserviceaccount@autoexcel-405401.iam.gserviceaccount.com\n3. Now give a small context for your business using context ".....".\n4. Give the columns of excel sheet in order using columns ".....".\n5. Set sheet name using sheet "..."\n6. Now you can send unsorted data to the bot and it will be sorted and added to the sheet.\n`
        
        """

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
    "context": os.environ.get('B'),
    "columns": os.environ.get('C'),
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
    row_data= requests.post(url_row+f"/{os.environ.get('A')}", json=response_data)
    print(row_data)
    
    return   format_message(row_data.json())


def format_message(data):
    formatted_message = "A new row was added:\n"
    for key, value in data.items():
        formatted_message += f"{key.capitalize()} - {value}\n"
    return formatted_message.rstrip('\n')