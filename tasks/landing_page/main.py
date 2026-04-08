from fastapi import FastAPI

app = FastAPI()

class FeatureCard(BaseModel):
    """
    Feature card model
    """
    title: str
    description: str
    icon: str

@app.get('/')
def read_root():
    """
    Returns a message for the landing page
    """
    return {'message': 'Landing page'}