from dotenv import load_dotenv
from fastapi import FastAPI
from client.generate import generate_image
from client.describe import describe_image
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import ssl


load_dotenv()

class GenerateQuery(BaseModel):
    urls: List[str]
    prompt: str

app = FastAPI()

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('/etc/letsencrypt/live/rembrandt.alexfprowe.com/fullchain.pem', keyfile='/etc/letsencrypt/live/rembrandt.alexfprowe.com/privkey.pem')

origins = ['http://localhost:5173', 'https://alexfprowe.com/rembrandt']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def ping():
    return {"message": "pong"}

@app.post('/generate')
async def generate(query: GenerateQuery):
    print('Grabbing image qualities...')
    qualities = describe_image(query.urls)
    print('Generating image...')
    photo_url = generate_image(query.prompt, qualities)
    return {"success": True, "url": photo_url}
