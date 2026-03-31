from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def read_root():
    html_content = "<html><body><h1>Santos Gómez</h1><p>Field IT Specialist en bioMérieux</p><p>Experto en HL7 FHIR, Docker y AWS</p></body></html>"
    return HTMLResponse(content=html_content, status_code=200)