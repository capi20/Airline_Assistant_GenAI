import base64
from io import BytesIO
from PIL import Image
from config import openai
from prompts import gen_image_message

def image_generator(city):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=gen_image_message(city),
        size="1024x1024",
        n=1,
        response_format="b64_json",
    )

    image_base64 = response.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    return Image.open(BytesIO(image_data))
    

