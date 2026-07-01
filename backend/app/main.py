from fastapi import FastAPI

app = FastAPI(
    title="Universal Media Transcriber API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }