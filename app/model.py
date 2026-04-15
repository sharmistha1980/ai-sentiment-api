from transformers import pipeline

class SentimentModel:
    def __init__(self):
        self.pipeline = None

    def load_model(self):
        # Using a lightweight, fast model perfect for basic text classification
        self.pipeline = pipeline(
            "sentiment-analysis", 
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def predict(self, text: str):
        if not self.pipeline:
            raise RuntimeError("Model is not loaded. Check startup logs.")
        
        # The pipeline returns a list of dicts, e.g., [{'label': 'POSITIVE', 'score': 0.99}]
        return self.pipeline(text)[0]

# Create a single instance to be used across the app
nlp_model = SentimentModel()