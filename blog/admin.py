from django.contrib import admin

# Register your models here.
'''
Django的admin界面是动态生成的，
只有明确告诉Django哪些模型应该在admin界面中显示时，
这些模型才会出现。
'''
from .models import Post, Chapter

# Register your models here.
#使用admin.site.register()函数来注册Post模型，使其在admin界面中可用。
admin.site.register(Post)
admin.site.register(Chapter)