from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("Google_api_key")

# Configure the Google Generative AI
if api_key:
    genai.configure(api_key=api_key)
else:
    raise HTTPException(status_code=500, detail="Google API key not found or incorrect")

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/generate")
async def generate_text(request: TextRequest):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(request.text)
        return {"generated_text": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
