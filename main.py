from fastapi import FastAPI

app = FastAPI(
    title="Task Management App",
    description="Task management using APIs",
    version="1.0.0"
)

@app.get("/")
def home():
    return "Welcome to Task Management App!"

@app.get("/health")
def health():
    return{
        "status":"Ok"
    }