from dotenv import load_dotenv
from fastapi import FastAPI
from client.generate import generate_image
from client.describe import describe_image
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

class Item(BaseModel):
    url: str
    prompt: str

app = FastAPI()

origins = ['http://localhost:5173']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/generate')
async def generate(query: Item):
    qualities = describe_image(query.url)
    photo_url = generate_image(query.prompt, qualities)
    return {"success": True, "url": photo_url}
