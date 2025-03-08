from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load the trained model and tokenizer
MODEL_PATH = "fake_news_model"
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

# Initialize FastAPI app
app = FastAPI()

# Define input data model
class NewsInput(BaseModel):
    article: str  # Expect a single text input

@app.post("/predict")
def predict_news(news: NewsInput):
    # Tokenize input article
    inputs = tokenizer(news.article, return_tensors="pt", padding=True, truncation=True)

    # Get model prediction
    outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()

    # Return prediction
    return {"prediction": "Fake" if prediction == 1 else "Real"}
