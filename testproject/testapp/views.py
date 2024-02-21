from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import PostForm
from .models import Post
import bcrypt

# Create your views here.

def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=PostForm()
    return render(request,'create_post.html',{'form':form})


def post_list(request):
    posts=Post.objects.all()
    return render(request, 'post_list.html',{'posts':posts})


def delete_post(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html',{'post':post})

def home(request):
 return render(request,'home.html')


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            before_hashed=request.POST['password1']
            hashed_password=bcrypt.hashpw(before_hashed.encode('utf-8'), bcrypt.gensalt())

            user = User.objects.create_user(
                username=request.POST['username'],
                password=hashed_password.decode('utf-8'),
            )
            
            auth.login(request, user)

            return render(request, 'log_success.html',{'user':user})
          
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":

        before_checked=request.POST['password']
        decoded=bcrypt.checkpw(before_checked.encode('utf-8'), User.encode('utf-8'))
        username = request.POST['username']
    
        def name_auth(username):
            global User
            if username==User.username:
                return True
            else:
                return False


        if name_auth is True:
            auth.login(request, username)
            return render(request, 'log_success.html',{'user':username})           
        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })
    else:
        return render(request, "login.html")
    
def log_success(request):
    user = request.username
    return render(request, 'log_success.html',{'user':user})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # redirect('home')
    return render(request,'login.html')

def user_information(request):
    print(request.user.username)
    # test
    print(request.user.email)
    # test@yahoo.co.jp
    print(request.user.is_active)
    # True
    print(request.user.is_staff)
    # False
    print(request.user.is_superuser)
    # False