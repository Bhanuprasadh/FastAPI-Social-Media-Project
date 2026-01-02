from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

text_posts = {1: {"title": "New Post", "content": "cool text post"}}

@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)