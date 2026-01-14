from fastapi import FastAPI

app = FastAPI()

@app.get('/f1')
def hello():
    return {"Message": "hello-world"}