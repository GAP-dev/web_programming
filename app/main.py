from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{ "message": "Hello Bosman!"}

@app.get("/home")
def home():
    return { "message": "Bye Bosman!" }