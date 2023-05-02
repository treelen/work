from django.shortcuts import render
from apps.settings.models import Settings
from apps.blog.models import Blog

def index(request):
    settings = Settings.objects.latest('id')
    blog = Blog.objects.order_by('-id')
    if request.user == post.user:
        if request.method == 'POST':
            blog_logo = request.FILES.get('blog_logo')
            blog_title = request.POST.get('blog_title')
            blog_description=request.POST.get('blog_description')
            try:
                blog.blog_title = text
                blog.blog_description = text
                blog.blog_logo = file
                blog.save()

                return redirect('index')
            except:
                blog.blog_title = text
                blog.blog_description = text
                blog.blog_logo = file
                blog.save()
                return redirect('index')
            else:
                blog.blog_title = text
                blog.blog_description = text
                blog.blog_logo = file
                blog.save()
    else:
        return redirect('index')

    context = {
        'blog': blog,
        'settings': settings
    }
    return render(request, 'settings/index.html', context)
            