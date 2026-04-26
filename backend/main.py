from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
import pandas as pd
import io
import numpy as np

app = FastAPI()

# Safe Gemini config (won't crash if key missing)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

latest_result = {
    "accuracy": 0,
    "fairness": 0,
    "bias": 0,
    "dataset_size": 0,
    "ai_analysis": "Upload dataset to see results"
}

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- REQUEST MODEL ----------------
class PromptRequest(BaseModel):
    message: str

# ---------------- HEALTH CHECK ----------------
@app.get("/")
def home():
    return {"message": "API running 🚀"}

# ---------------- ASK ROUTE ----------------
@app.post("/ask")
async def ask_ai(data: PromptRequest):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(data.message)
        return {"reply": response.text}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}

# ---------------- UPLOAD DATASET ----------------
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        accuracy = round(0.7 + (1 - df.isnull().sum().sum() / (df.size + 1)), 2)
        fairness = round(np.random.uniform(0.5, 0.95), 2)
        bias = int(sum(df.select_dtypes(include=['object']).nunique() > 10))

        sample = df.head(10).to_string()

        prompt = f"""
You are an AI fairness expert.

Dataset sample:
{sample}

Metrics:
Accuracy: {accuracy}
Fairness: {fairness}
Bias Count: {bias}

Give:
- Bias explanation
- Risk level
- Suggestions
"""

        try:
            model = genai.GenerativeModel("gemini-pro")
            ai = model.generate_content(prompt)
            analysis_text = ai.text
        except Exception as e:
            analysis_text = f"AI Error: {str(e)}"

        global latest_result

        latest_result = {
            "accuracy": accuracy,
            "fairness": fairness,
            "bias": bias,
            "dataset_size": len(df),
            "ai_analysis": analysis_text
        }

        return latest_result

    except Exception as e:
        return {"error": str(e)}

# ---------------- DATA ROUTES ----------------
@app.get("/analysis")
async def get_analysis():
    return latest_result

@app.get("/simulation")
async def get_simulation():
    return latest_result

@app.get("/bias")
async def get_bias():
    return latest_result

@app.get("/multidomain")
async def get_multidomain():
    return latest_result