from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def generate_image(prompt, qualities):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    prompt_context= " with the following image style qualities: " + qualities

    response = client.images.generate(
        model="dall-e-3",
        prompt= prompt + prompt_context,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url
