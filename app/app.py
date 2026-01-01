from fastapi import FastAPI
import uvicorn

app = FastAPI()

text_posts = {}

@app.get("/posts")
def get_all_posts():
    return text_posts





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)