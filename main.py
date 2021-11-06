from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(post: Post):
    # Even we can extract data to easy
    print(post)
    print(post.title)
    print(post.published)
    print(post.rating)
    return {
        "message": "Succesfully created posts",
        "post": post,
    }