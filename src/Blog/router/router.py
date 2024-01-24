from fastapi import APIRouter
from src.Blog.service.service import BlogService
from src.Blog.model.model import Blog, BlogUpdate

blog = APIRouter(prefix='/api/v1/blogs', tags=['Blogs'])


@blog.get('/')
def get_blog(blog_id = 'all'):
    return BlogService.get(blog_id)
    

@blog.get('/{blog_id}')
def get_blog(blog_id : int):
    return BlogService.get(blog_id)
     


@blog.post('/')
def create_blog(blog:Blog):
    return BlogService.post(blog_content=blog)

@blog.put('/{blog_id}')
def update_post(blog_id: int, new_content:BlogUpdate):
    return BlogService.put(blog_id=blog_id, new_content=new_content)

@blog.delete('/{blog_id}')
def update_post(blog_id:int):
    return BlogService.delete(blog_id=blog_id)