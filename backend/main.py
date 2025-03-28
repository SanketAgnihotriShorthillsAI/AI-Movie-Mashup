# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from mashup_logic import build_prompt, build_dialogue_prompt, build_scene_prompt
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro-latest")

class MashupRequest(BaseModel):
    movie1: str
    movie2: str
    genre: str
    extra_context: str = ""

class DialogueRequest(BaseModel):
    movie1: str
    movie2: str
    genre: str
    scene_desc: str

class SceneRequest(BaseModel):
    movie1: str
    movie2: str
    genre: str
    scene_idea: str

@app.post("/generate")
async def generate_mashup(req: MashupRequest):
    prompt = build_prompt(req.movie1, req.movie2, req.genre, req.extra_context)
    try:
        response = model.generate_content(prompt)
        result_text = response.candidates[0].content.parts[0].text
        return {"output": result_text}
    except Exception as e:
        return {"error": f"Gemini API call failed: {str(e)}"}

@app.post("/dialogue")
async def generate_dialogue(req: DialogueRequest):
    prompt = build_dialogue_prompt(req.movie1, req.movie2, req.genre, req.scene_desc)
    try:
        response = model.generate_content(prompt)
        result_text = response.candidates[0].content.parts[0].text
        return {"output": result_text}
    except Exception as e:
        return {"error": f"Gemini API call failed: {str(e)}"}

@app.post("/scene")
async def generate_scene(req: SceneRequest):
    prompt = build_scene_prompt(req.movie1, req.movie2, req.genre, req.scene_idea)
    try:
        response = model.generate_content(prompt)
        result_text = response.candidates[0].content.parts[0].text
        return {"output": result_text}
    except Exception as e:
        return {"error": f"Gemini API call failed: {str(e)}"}
