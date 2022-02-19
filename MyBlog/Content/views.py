from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import is_valid_path
from .models import *
from .models import Blog, Comment
from .forms import  CommentForm
from django.shortcuts import  get_object_or_404
from .forms import  UserRegistrationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def index(request):
    category = Category.objects.all()
    posts =Blog.objects.all()
    
    return render(request,'Content/posts.html',{'posts':posts,'category':category})


def category_by_id(request,id):

    category = Category.objects.all()
    posts = Blog.objects.filter(category_id = id)
    return render(request,'Content/posts.html',{'posts':posts,'category':category})



def post_by_id(request,id):
    post = Blog.objects.get(id = id)
    category = Category.objects.all()
    comment_form = CommentForm()
    comments = Comment.objects.all()

    if request.method == 'POST':
    # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm() 

    return render(request,'Content/one_post.html',{'post':post,'category':category,'comment_form':comment_form,
                  'comments': comments,
                  'comment_form': comment_form})

            




# Регистрация



def register(request):
    category = Category.objects.all()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
        
            login(request, new_user)

            return redirect('index')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'Content/register.html', {'user_form': user_form,'category':category})



# Автаризация

def user_login(request):
    posts =Blog.objects.all()
    category = Category.objects.all()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'Content/posts.html',{'posts':posts,'category':category})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'Content/login.html', {'form': form,'category':category})


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('index')