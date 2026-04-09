from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="mlops-scaffold")

class PredictRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "barsha"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: PredictRequest):
    # placeholder model logic
    score = len(req.text) / 100
    return {"label": "positive" if score > 0.2 else "negative", "score": score}