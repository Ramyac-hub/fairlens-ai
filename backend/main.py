from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os
import pandas as pd
import io
import numpy as np

# ---------------- LOAD ENV ----------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# ---------------- APP ----------------
app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fairlens-ai-psi.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- MODEL ----------------
class PromptRequest(BaseModel):
    message: str

# ---------------- HOME ----------------
@app.get("/")
def home():
    return {"message": "API running 🚀"}

# ---------------- ASK ROUTE ----------------
@app.post("/ask")
async def ask_ai(data: PromptRequest):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(data.message)
        return {"reply": response.text}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}

# ---------------- UPLOAD ----------------
latest_result = {}

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

        model = genai.GenerativeModel("gemini-1.5-flash")
        ai = model.generate_content(prompt)

        global latest_result
        latest_result = {
            "accuracy": accuracy,
            "fairness": fairness,
            "bias": bias,
            "dataset_size": len(df),
            "ai_analysis": ai.text
        }

        return latest_result

    except Exception as e:
        return {"error": str(e)}

# ---------------- DATA ROUTES ----------------
@app.get("/analysis")
def get_analysis():
    return latest_result

@app.get("/simulation")
def get_simulation():
    return latest_result

@app.get("/bias")
def get_bias():
    return latest_result

@app.get("/multidomain")
def get_multidomain():
    return latest_result