# app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define input model
class InputData(BaseModel):
    text: str

# Example function you want to expose
def process_text(text):
    return text[::-1]  # Example: reverse the input

# API endpoint
@app.post("/api/process")
async def api_process(data: InputData):
    result = process_text(data.text)
    return {"result": result}
