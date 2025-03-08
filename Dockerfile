FROM python:3.9

# Set the working directory inside the container
WORKDIR /Fake-News-Detector

# Copy the current directory (where Dockerfile is) to /Fake-News-Detector
COPY . /Fake-News-Detector

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port where the app will run
EXPOSE 8000

# Command to run the fake news detector (FastAPI) with Uvicorn
CMD ["uvicorn", "fakeNewsDetector:app", "--host", "0.0.0.0", "--port", "8000"]
