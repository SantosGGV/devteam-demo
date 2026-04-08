from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    """Return a message.

    Args:
        None

    Returns:
        dict: A dictionary with a message.
    """
    return {'message': 'Hello World'}