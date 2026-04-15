from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
from app.model import nlp_model

# This lifespan context ensures the model loads exactly once when the server starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading ML model...")
    nlp_model.load_model()
    print("Model loaded successfully!")
    yield
    print("Shutting down and cleaning up...")

app = FastAPI(title="Sentiment API", lifespan=lifespan)

# Define the expected JSON input structure
class PredictRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API. Go to /docs to test it."}

@app.get("/health")
def health_check():
    # Quick check to ensure the model pipeline actually exists in memory
    is_ready = nlp_model.pipeline is not None
    return {"status": "healthy" if is_ready else "loading", "model_ready": is_ready}

@app.post("/predict")
def predict_sentiment(request: PredictRequest):
    # Pass the text to our model
    prediction = nlp_model.predict(request.text)
    
    return {
        "text": request.text,
        "label": prediction["label"],
        "confidence": round(prediction["score"], 4)
    }