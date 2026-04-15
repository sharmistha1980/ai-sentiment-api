# AI Sentiment Analysis API 🚀

A production-ready, containerized backend API that serves a Hugging Face machine learning model using FastAPI. 

This project demonstrates a complete end-to-end ML deployment pipeline, from local development to cloud hosting via Docker and automated CI/CD.

## 🛠️ Tech Stack
* **Framework:** FastAPI, Uvicorn, Python 3.10
* **Machine Learning:** Hugging Face Transformers, PyTorch (CPU-optimized)
* **Model:** `distilbert-base-uncased-finetuned-sst-2-english`
* **DevOps:** Docker, GitHub Actions (CI/CD), Render

## ✨ Features
* **Singleton Model Loading:** The ML model is loaded into memory exactly once during the server's lifespan, completely eliminating cold-start latency for incoming inference requests.
* **Fully Containerized:** Packaged into a lightweight Linux Docker container, ensuring cross-platform consistency.
* **Automated CI/CD:** Integrated with GitHub Actions to automatically validate Python syntax and dependencies on every push.
* **Interactive API Docs:** Built-in Swagger UI for easy endpoint testing.

## 🚀 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/`      | Welcome message and API root. |
| `GET`  | `/health`| Health check verifying the ML model is loaded and ready. |
| `POST` | `/predict`| Accepts a text string and returns the predicted sentiment (POSITIVE/NEGATIVE) with a confidence score. |

## 💻 Local Setup (Without Docker)
1. Clone the repository:
   
   git clone [https://github.com/yourusername/ai-sentiment-api.git](https://github.com/yourusername/ai-sentiment-api.git)
   cd ai-sentiment-api
   
2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt
Run the development server:

uvicorn app.main:app --reload
Visit http://localhost:8000/docs to test the API.

🐳 Docker Setup
To run the fully containerized version locally:

# Build the image
docker build -t sentiment-api .

# Run the container
docker run -d -p 8000:8000 --name live-api sentiment-api

