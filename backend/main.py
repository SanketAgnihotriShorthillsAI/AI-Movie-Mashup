# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from mashup_logic import build_prompt, build_dialogue_prompt, build_scene_prompt, build_quick_mashup_prompt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini API setup

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Check if the key is loaded correctly
api_key = os.getenv("GEMINI_API_KEY")
print("key: ", api_key)  # Optional for debugging, remove in production

# Pass the actual API key
genai.configure(api_key=api_key)

# Create the model instance
model = genai.GenerativeModel('gemini-1.5-pro-latest')


# Models
class MashupRequest(BaseModel):
    genre: str
    character1: str
    character2: str

class DialogueRequest(BaseModel):
    genre: str
    character1: str
    character2: str

class SceneRequest(BaseModel):
    genre: str
    character1: str
    character2: str

class QuickMashupRequest(BaseModel):
    user_input: str

# Routes
@app.post("/mashup")
async def mashup(req: MashupRequest):
    prompt = build_prompt(req.genre, req.character1, req.character2)
    try:
        response = model.generate_content(prompt)
        result_text = response.candidates[0].content.parts[0].text
        return {"output": result_text}
    except Exception as e:
        return {"error": f"Gemini API call failed: {str(e)}"}

@app.post("/dialogue")
async def dialogue(req: DialogueRequest):
    prompt = build_dialogue_prompt(req.genre, req.character1, req.character2)
    try:
        response = model.generate_content(prompt)
        result_text = response.candidates[0].content.parts[0].text
        return {"output": result_text}
    except Exception as e:
        return {"error": f"Gemini API call failed: {str(e)}"}

@app.post("/scene")
async def scene(req: SceneRequest):
    prompt = build_scene_prompt(req.genre, req.character1, req.character2)
    try:
        response = model.generate_content(prompt)
        result_text = response.candidates[0].content.parts[0].text
        return {"output": result_text}
    except Exception as e:
        return {"error": f"Gemini API call failed: {str(e)}"}

@app.post("/quick_mashup")
async def quick_mashup(req: QuickMashupRequest):
    prompt = build_quick_mashup_prompt(req.user_input)
    try:
        response = model.generate_content(prompt)
        result_text = response.candidates[0].content.parts[0].text
        return {"output": result_text}
    except Exception as e:
        return {"error": f"Gemini API call failed: {str(e)}"}
