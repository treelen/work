from django.shortcuts import render
from apps.settings.models import Settings 
from apps.blog.models import Blog
from django.views.generic.base import View
# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    if request.method == 'POST':
        if create_blog in request.POST:
            blog_title=request.POST.get('blog_title')
            blog_description=request.POST.get('blog_description')
            blog_logo=request.FILES.get('blog_logo')
            try:
                blog = Blog.objects.create(blog_title = blog_title,blog_description=blog_description,blog_logo=blog_logo,user = request.user)
                blog.save()
            except:
                blog = Blog.objects.create(blog_title = blog_title,blog_description=blog_description,blog_logo=blog_logo,user = request.user)
                blog.save()
    context ={
        'blog':blog
    }
    return render(request,'blog/blog.html',context)



class Blog_detail(View):
    def get(self,request,id):
        blog = Blog.objects.get(id=id)
        context = {
            'blog':blog
        }
        return render(request,'blog/blog_detail.html',context)


    
def blog_delete(request, id):
    settings = Settings.objects.latest('id')
    blog = Blog.objects.get(id=id)
    if request.user == blog.user:
        if request.method == 'POST':
            blog.delete()
            return redirect('index')

    else:
        return redirect('index')
    return render(request, 'blog/blog_delete.html')