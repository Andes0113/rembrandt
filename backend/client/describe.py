from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def describe_image(url):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe the style of this image as a comma-separated list of descriptors, which can include photographic techniques, composition styles, moods, genres, or type of scenes. Include the color scheme. Do not describe the content of the image."},
            {
            "type": "image_url",
            "image_url": {
                "url": url,
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    return response.choices[0].message.content
