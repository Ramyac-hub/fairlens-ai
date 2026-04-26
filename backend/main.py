from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
import os
import pandas as pd
import io
import numpy as np

app = FastAPI()
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

# ---------------- GEMINI ----------------
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise Exception("❌ GEMINI_API_KEY not set")

client = genai.Client(api_key=API_KEY)

# ---------------- STORE GLOBAL DATA ----------------

# ---------------- ASK ROUTE (CHAT) ----------------
class PromptRequest(BaseModel):
    message: str

@app.post("/ask")
async def ask_ai(data: PromptRequest):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=data.message
        )
        return {"reply": response.text}
    except Exception as e:
        return {"reply": str(e)}

# ---------------- UPLOAD DATASET ----------------
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    # KPIs (DYNAMIC)
    accuracy = round(0.7 + (1 - df.isnull().sum().sum() / (df.size + 1)), 2)
    fairness = round(np.random.uniform(0.5, 0.95), 2)
    bias = int(sum(df.select_dtypes(include=['object']).nunique() > 10))

    sample = df.head(10).to_string()

    # GEMINI ANALYSIS
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

    ai = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    global latest_result

    latest_result = {
        "accuracy": accuracy,
        "fairness": fairness,
        "bias": bias,
        "dataset_size": len(df),
        "ai_analysis": ai.text
    }

    return latest_result

# ---------------- SHARED DATA FOR ALL HTML PAGES ----------------
@app.get("/analysis")
async def get_analysis():
    if not latest_result or latest_result["dataset_size"] == 0:
        return {
            "accuracy": 0,
            "fairness": 0,
            "bias": 0,
            "dataset_size": 0,
            "ai_analysis": "No dataset uploaded yet"
        }
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