from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
async def read_hello(name: str):
    return JSONResponse(content={"message": f"Hello, {name}!"}, media_type="application/json")