from enum import unique
from wsgiref.validate import validator
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator



# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length =80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(null=True)

    def fullname(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.fullname()
    
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length = 80)
    date = models.DateField(auto_now =True)
    images =models.ImageField(upload_to="posts", null=True)
    # image = models.CharField(max_length = 120,null=True)
    slug = models.SlugField(unique=True ,default ="",null=False,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)],null=True)
    author = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL,related_name = "posts")
    tag = models.ManyToManyField(Tag)


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=450)
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name="comments")


