from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/mock_get/")
async def mock_get(input_string: str):
    return {"mock_get_response": input_string}


@app.post("/mock_post/")
async def mock_post(input_string: str):
    return {"mock_post_response": input_string}
