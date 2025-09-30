import json
from prompts import system_message 
from config import openai, MODEL
from tools import tools, get_ticket_price
from image import image_generator

def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    city = args.get('destination_city')
    price = get_ticket_price(city)
    response = {
        "role": "tool",
        "content": json.dumps({"destination_city": city, "price": price}),
        "tool_call_id": tool_call.id
    }

    return response, city

def chat(history):
    messages = [{"role": "system", "content": system_message}] + history
    response = openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    image = None

    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        image = image_generator(city)
        response = openai.chat.completions.create(model=MODEL, messages=messages)

    reply = response.choices[0].message.content
    history += [{"role": "assistant", "content": reply}]

    return history, image
        
