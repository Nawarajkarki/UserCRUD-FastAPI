



class PatternError(Exception):
    def __init__(self, pattern):
        self.pattern = pattern        
    
    
class TagsError(Exception):
    def __init__(self, tag):
        self.tag = tag
    
        
 
