from fastapi import FastAPI

app = FastAPI(title="TestSaber")


@app.get("/")
async def root():
    return {"message": "Hello World"}

