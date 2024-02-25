from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def describe_image(urls):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    content = []
    content.append({
        "type": "text",
        "text": "Describe the style of this image as a comma-separated list of descriptors, which can include photographic techniques, composition styles, moods, genres, or type of scenes. Include the color scheme. Do not describe the content of the image."
    })
    for url in urls:
        content.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": url,
                },
            }
        )

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        max_tokens=300,
    )

    return response.choices[0].message.content
