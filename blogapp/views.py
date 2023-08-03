from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def single(request):
    return render(request,'single.html')

def typography(request):
    return render(request,'typography.html')

from blogapp.forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 
 
def register(request):	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('blogapp:login_reg')


	context = { 'form': form }
	return render (request, 'signin/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('blogapp:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'signin/login.html', context)

def logoutuser(request):
	logout(request)
	# return redirect('blogapp:login_reg')
	return redirect('blogapp:login_reg')


@login_required(login_url = 'blogapp:login_reg')
def index(request):
	return render (request,"index.html", context = {})


from .forms import BlogPostForm
from .models import BlogPost

def blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            blog_obj = form.instance
            return render(request, 'blogpost.html', {'form': form, 'blog_obj': blog_obj})
    else:
        form = BlogPostForm()
    return render(request, 'blogpost.html', {'form': form})


def blogs(request):
    all_blogs=BlogPost.objects.all()
    context={'all_blogs':all_blogs}
    return render(request, 'blog.html', context)
