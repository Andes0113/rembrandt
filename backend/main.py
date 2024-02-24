from dotenv import load_dotenv
from fastapi import FastAPI
from client.generate import generate_image

load_dotenv()


app = FastAPI()

@app.get('/')
async def root():
    url = generate_image()
    return {"success": True, "url": url}
