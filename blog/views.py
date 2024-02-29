from django.shortcuts import render

# Create your views here.创建一个视图来显示一个表单，并允许用户输入新的文章
from django.shortcuts import render, get_object_or_404
from .models import Post, Chapter
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from .forms import PostForm

def home(request):
    return render(request, 'blog/home.html', {})
'''
def post_new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.POST.get('image')
        post = Post(title=title, content=content, pub_date=timezone.now())
        post.save()
        return HttpResponseRedirect('/')
    return render(request, 'blog/post_edit.html', {})
'''
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
#创建一个视图来显示文章
def post_list(request):
    posts = Post.objects.all()  # 获取所有文章
    return render(request, 'blog/post_list.html', {'posts': posts})

'''#创建文章详情视图
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    return render(request, 'blog/post_detail.html', {'post': post, 'prev_post': prev_post, 'next_post': next_post})
'''

'''import markdown

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 将 Markdown 转换为 HTML
    post.content = markdown.markdown(post.content, extensions=['fenced_code', 'codehilite'])
    
    # 获取前一篇和后一篇文章
    prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()

    # 确保将所有必要的变量传递给模板
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }

    return render(request, 'blog/post_detail.html', context)
'''
'''import markdown2

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Using markdown2 to convert Markdown to HTML with MathJax support
    post.content = markdown2.markdown(post.content, extras=['fenced-code-blocks', 'code-friendly', 'mathjax'])

    # Get the previous and next posts
    prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()

    # Ensure all necessary variables are passed to the template
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }

    return render(request, 'blog/post_detail.html', context)

'''

import markdown_it

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 使用 markdown-it-py 转换 Markdown 到 HTML
    md = markdown_it.MarkdownIt()
    post.content = md.render(post.content)

    # 获取前一篇和后一篇文章
    prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()

    # 确保将所有必要的变量传递给模板
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }

    return render(request, 'blog/post_detail.html', context)

def chapter_list(request):
    chapters = Chapter.objects.all()
    return render(request, 'blog/chapter_list.html', {'chapters': chapters})

def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    return render(request, 'blog/chapter_detail.html', {'chapter': chapter})

def chapter_articles(request, pk):
    chapter = Chapter.objects.get(pk=pk)
    articles = chapter.posts.all()  # 获取这一章节的所有文章
    # 创建HTML字符串
    articles_html = ''.join([f'<li><a href="{article.get_absolute_url()}">{article.title}</a></li>' for article in articles])
    return HttpResponse(articles_html)