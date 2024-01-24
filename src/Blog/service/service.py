from src.Blog.repository.repository import BlogRepository
from src.User.repository.repository import UserRepository
from datetime import datetime
class BlogOperation():
    
    def __init__(self):
        self.blog = BlogRepository()
        self.user_repo = UserRepository()
        self.now = datetime.now()
    
    def get(self, blog_id):
        resp = self.blog.get(blog_id)
        return resp
    
    def post(self, blog_content):
        author = blog_content.author

        print(self.user_repo.get(author))
        user_check = (self.user_repo.get(author))
        
        
        if user_check.status_code == 404:
            print(self.user_repo.get(author))
            return {
                "msg" : "Failed",
                "Error" : "invalid username"
            }
            
        
        resp = self.blog.post(now = self.now, blog_content=blog_content)
        return resp
    
    
    def put(self, blog_id, new_content):
        return self.blog.put(blog_id=blog_id, blog_content=new_content, now=self.now)
    
    def delete(self, blog_id):
        return self.blog.delete(blog_id=blog_id, now=self.now)

BlogService = BlogOperation()