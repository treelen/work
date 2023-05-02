from django.shortcuts import render,redirect
from apps.users.models import User
from apps.settings.models import Settings 

def register(request):
    settings = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        profile_image = request.FILES.get('profile_image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            try:
                user = User.objects.create(username = usernmae,email=email,phone_number=phone_number,profile_image=profile_image)
                user.set_password(password)
                user.save()
                user= User.objects.get(username = username)
                user = authenticated(username = username, password=passowrd)
                login(request,user)
                return redirect('index.html',user.username)
            except:
                return redirect('register')
            
    context = {
        'settings':settings
    }
    return render(request,'users/register.html',context)
        
def login(request):
    settings = Settings.objects.latest('id')
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = User.objects.get(username=username)
        user =authenticate(username=username ,password=password)
        login(request,user)     
            
        return redirect('index')
    context ={
        'settings':settings
    }
    return render (request ,'users/login.html' ,context)