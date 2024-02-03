from django.db import models
from baloba.utils.base import BaseModel
from ckeditor.fields import RichTextField

# Create your models here.
class Author(BaseModel):
    author_name = models.CharField(max_length=20, verbose_name='Name of the Author', help_text='*Maximum 20 characters')
    description = models.TextField(verbose_name='Description of the blog', null=False, blank=True)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'All Authors'
    
    def __str__(self):
        return self.author_name

class Category(BaseModel):
    category_name = models.CharField(max_length=20, verbose_name='Name of the Category', help_text='*Maximum 20 characters')
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'All Category'
    
    def __str__(self):
        return self.category_name
    
class Tags(BaseModel):
    name = models.CharField(max_length=20,verbose_name="tag name", help_text="max 20 characters")
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "All Tags"
    
    def __str__(self):
        return self.name        
class Blogs(BaseModel):
    # BLOG_TYPES = (
    #     (0, 'Choose'),
    #     (1, 'Tech'),
    #     (2, 'Food'),
    #     (3, 'Travel'),
    #     (4, 'Lifestyle'),
    # )
    
    title = models.CharField(max_length=100, verbose_name='Title of the blog', help_text='Maximum 100 characters')
    description = RichTextField(verbose_name='Description of the blog', null=False, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author of the Blog', null=True)
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='name of blog category', null=True)
    is_check = models.BooleanField(default=False, verbose_name='Is the Blog checked?')
    poster = models.ImageField(upload_to='blog/poster', verbose_name="Poster of Blog", null=True, blank=True)
    tag_name = models.ManyToManyField(Tags)
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'All Blogs'
    
    def __str__(self):
        return self.title