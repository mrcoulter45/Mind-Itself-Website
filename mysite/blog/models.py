from django.db import models

#each class is like a table in the database
#each class var is like a col

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title
