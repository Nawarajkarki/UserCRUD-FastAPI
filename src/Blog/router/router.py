from fastapi import APIRouter


Blog = APIRouter(prefix='/api/v1/blogs', tags=['Blogs'])


@Blog.get('/')
def home():
    return {
        "msg" : "this is home of blog"
    }