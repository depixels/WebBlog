from django.db import models
from django.urls import reverse 
# Create your models here. 设计数据库模型
class Chapter(models.Model):
    title = models.CharField(max_length=200)
    # 其他可能的章节字段...

    def __str__(self):
        return self.title
'''
class Post(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='posts', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    code = models.TextField(blank=True)  # 添加一个用于存储代码的字段

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])
'''
class Post(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='posts', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()  # 存储 Markdown 文本
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    code = models.TextField(blank=True)  # 添加一个用于存储代码的字段

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])
