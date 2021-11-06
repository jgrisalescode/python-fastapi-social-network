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

my_posts = [
    {"title": "Awesome post", "content": "An awesome content too", "id": 1},
    {"title": "Favorite foods", "content": "I like pizza", "id": 2}
]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    # Even we can extract data to easy
    print(post)
    print(post.dict())
    print(post.title)
    print(post.published)
    print(post.rating)
    return {
        "message": "Succesfully created posts",
        "post": post,
    }