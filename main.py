import uvicorn
from fastapi import FastAPI

from app.routers import book_router

app = FastAPI()
app.include_router(book_router)


@app.get("/")
async def get_root():
    return {"response": "Hello, ReadIt!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
