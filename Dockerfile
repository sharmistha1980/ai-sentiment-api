# Use official lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file first to leverage Docker layer caching
COPY ./requirements.txt /code/requirements.txt

# Install dependencies (ignoring cache to keep image size small)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Pre-download the Hugging Face model during the image build 
# This prevents the container from downloading it every time it restarts
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')"

# Copy the rest of the application code
COPY ./app /code/app

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]