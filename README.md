# Fake-News-Detector

Project: Develop a deep learning model that can classify news articles as real or fake based on textual content.

Tech Stack:
   - PyTorch: training a deep learning model (BERT: machine learning framework that helps computers understand the meaning of text)
   - Hugging Face Transformers: Use BERT for better NLP performance
   - FastAPI: Serve the model as a REST API.
   - Docker: Containerize the application for easy deployment

Step 1: Data Collection & Preprocessing
  - get fake and true news datasets from https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets?resource=download 
  - Implement createNewsDataset.py --> add "label" columns to fake and true news datasets. "1" for all fake news, and "0" for all true news. Mix all news into one dataset and shuffle the columns.

Step 2: Train a Deep Learning Model
  - implement trainModel.py --> train the deep learning model, and save it.

Step 3: Build a REST API (FastAPI)
  - implement fakeNewsDetector.py --> users can use API calls to check if an article is fake or not.

Step 4: Containerize the App with Docker
  - implement a Docker file to package the app for better deployment.

How to run (bash):
   - python3 createNewsDataset.py
   - python3 trainModel.py
   - docker build -t fake-news-detector .
   - docker run -p 8000:8000 fake-news-detector

How to test:
   - curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"article": "Breaking: This is a fake news article!"}'
   - expected output: {"prediction": "Fake"} (Json)
