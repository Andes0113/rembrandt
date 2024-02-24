from openai import OpenAI
import os

def generate_image():
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    prompt_context="high quality tech company logo with the following subject:"

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt_context + "futuristic, blue and pink coloring, a cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url
