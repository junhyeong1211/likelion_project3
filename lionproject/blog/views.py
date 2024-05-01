from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogForm 

def home(request):
    blogs = Blog.objects.all()
    blog_num = len(blogs)
    return render(request, "home.html", {"blogs": blogs, "blog_num":blog_num})

def detail(request,id):
    blog=get_object_or_404(Blog,pk = id)
    return render(request, 'detail.html', {'blog': blog})

def new(request):
    form = BlogForm()
    return render(request, "new.html", {'form': form})

def create(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.pub_date = timezone.now()
        new_post.save()
        return redirect("detail", new_post.id)
    return redirect('home')

def edit(request,id):
    edit_blog= Blog.objects.get(id=id)
    return render(request, 'edit.html',{'blog':edit_blog})

def update(request, id):
    update_blog=Blog.objects.get(id=id)
    update_blog.title=request.POST['title']
    update_blog.writer= request.POST['writer']
    update_blog.body= request.POST['body']
    update_blog.pub_date= timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog=Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')

    