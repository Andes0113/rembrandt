from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

qualities = "vintage, advertisement, flat illustration, retro, bold colors, text integration, product promotion, character endorsement, commercial art, high contrast, warm color palette"
prompt_context= " with the following image style qualities: " + qualities

response = client.images.generate(
  model="dall-e-3",
  prompt= "a cat in a toaster" + prompt_context,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
