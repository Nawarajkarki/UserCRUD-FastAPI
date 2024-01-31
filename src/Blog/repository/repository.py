from src.entrypoint.database import blogs
from src.Blog.model.model import Blog, BlogUpdate

from fastapi import status, HTTPException
from fastapi.responses import JSONResponse



class InMemoryBlog():
    
    def __init__(self):
        self.blog = blogs
        self.blog_counter = 0
        
    
    def get(self, blog_id):
        try:
            if blog_id == 'all':
                return ({
                    'msg' : 'success',
                    'blogs' : self.blog
                })
                # return JSONResponse (
                #     details = {
                        
                #     'msg' : 'Success',
                #     "Blogs" : self.blog,
                #     },
                #     status_code = status.HTTP_200_OK
                # )
            if self.blog.get(blog_id) is None:
                raise HTTPException(
                    detail= {
                        'msg' : 'failed',
                        'Error' : "Blog id did not match"
                    },
                    status_code = status.HTTP_404_NOT_FOUND
                )
                
            return {
                "msg" : "Success",
                "Blog_content" : self.blog[blog_id],
                'status' : status.HTTP_200_OK
            }
        except Exception as e:
            return {'m' : "fail inrepo", 'error' : e}
        
        
        
        
    
    def post(self, blog_content : Blog, now):
        try:
            self.blog_counter += 1
            
            
            self.blog[self.blog_counter] = {
                'blog_id' : self.blog_counter,
                "author" : blog_content.author,
                'title' : blog_content.title,
                'content' : blog_content.content,
                'last_update' : now
                
            }
            
            return {
                'msg' : "Success",
                'blog_id' : self.blog_counter
            }
        
        except Exception as e:
            raise HTTPException(
                detail= "Failed",
                status_code = status.HTTP_501_NOT_IMPLEMENTED,
            )
            
    
    
    def put(self,blog_id,  blog_content : BlogUpdate, now):
        old_blog = self.blog.get(blog_id)
        
        if old_blog is None:
            return {
                'msg' : "Failed",
                "Error" : "Blog Id doesnot match",
                "status" : status.HTTP_404_NOT_FOUND
            }
            
        if blog_content.author is not None:
            return {
                'msg' : "Failed",
                "Error" : "Author cannot be changed",
                "status" : status.HTTP_400_BAD_REQUEST
            }
            
        if blog_content.title is not None:
            old_blog['title'] = blog_content.title
            old_blog['last_update'] = now
            
        if blog_content.content is not None:
            old_blog['content'] = blog_content.content
            old_blog['last_update'] = now
        
        return {
            "msg" : "Success",
            "Error" : "Blog Updated",
            "status" : status.HTTP_202_ACCEPTED
        }
        
    
    def delete(self, blog_id, now):
        blog = self.blog.get(blog_id)
        
        if blog is None:
            return {
                'msg' : "Failed",
                "Error" : "Blog Id doesnot match",
                "status" : status.HTTP_404_NOT_FOUND
            }
            
        del self.blog[blog_id]
        self.blog[blog_id] = {
            'Deleted At' : now
        }
        return {
            "msg" : "Success",
            "Error" : "Blog deleted",
            "status" : status.HTTP_202_ACCEPTED
        }
        
BlogRepository = InMemoryBlog