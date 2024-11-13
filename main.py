import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return(random.randint(1000,9999))
