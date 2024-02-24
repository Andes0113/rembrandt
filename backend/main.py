from dotenv import load_dotenv
from fastapi import FastAPI
from client.generate import generate_image
from client.describe import describe_image


load_dotenv()


app = FastAPI()

@app.get('/')
async def root():
    url = generate()
    return {"success": True, "url": url}

@app.post('/generate')
async def generate_image(url, prompt):
    qualities = describe_image(url)
    photo_url = generate_image(prompt, qualities)
    return {"success": True, "url": photo_url}
