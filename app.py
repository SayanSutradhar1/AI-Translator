from fastapi import FastAPI
from translator import translate_text
from pydantic import BaseModel

app = FastAPI(title="Text Translator API")

class TranslationRequest(BaseModel):
    text: str
    target_language: str

@app.get("/")
def root():
    return "Server is running"

@app.post("/translate")
async def translate(request: TranslationRequest):
    try:
        result = translate_text(request.text, request.target_language)
        return {"translated_text": result}
    except Exception as e:
        return {"error": str(e)}
    