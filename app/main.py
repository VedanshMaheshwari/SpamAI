from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import joblib
import PyPDF2
import os
import io
import re

# Load model and vectorizer
MODEL_PATH = "C:\\Users\\vedan\\Desktop\\Sem 7\\CyberML\\Assignment 1\\model\\spam_classifier.joblib"
VECTORIZER_PATH = "C:\\Users\\vedan\\Desktop\\Sem 7\\CyberML\\Assignment 1\\model\\tfidf_vectorizer.joblib"
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

app = FastAPI()

# Allow CORS for frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@app.post("/predict_pdf/")
async def predict_pdf(file: UploadFile = File(...)):
    try:
        # Read PDF file
        contents = await file.read()
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(contents))
        text = " ".join(page.extract_text() or '' for page in pdf_reader.pages)
        cleaned = clean_text(text)
        X = vectorizer.transform([cleaned])
        pred = model.predict(X)[0]
        label = "SPAM" if pred == 1 else "Non-SPAM"
        return JSONResponse({"result": label})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
