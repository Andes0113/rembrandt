from dotenv import load_dotenv
from fastapi import FastAPI
from client.generate import generate_image
from client.describe import describe_image
from pydantic import BaseModel


load_dotenv()

class Item(BaseModel):
    url: str
    prompt: str

app = FastAPI()

@app.get('/')
async def root():
    url = generate_image()
    return {"success": True, "url": url}

@app.post('/generate')
async def generate(query: Item):
    qualities = describe_image(query.url)
    photo_url = generate_image(query.prompt, qualities)
    return {"success": True, "url": photo_url}
