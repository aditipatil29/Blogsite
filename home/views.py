from django.shortcuts import render,redirect
from django.http import HttpResponse
#from .models import Author
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import Post,Contact
from .forms import Contactform

@login_required
def logoutuser(req):
    logout(req)
    return redirect('home:login')

def signup(req):
    if req.method=='POST':
        new_user=User.objects.create_user(
            username=req.POST.get("username"),
            email=req.POST.get("email"),
            password=req.POST.get("password"),
            first_name=req.POST.get("fname"),
            last_name=req.POST.get("lname")
        )
       
        #print(new_author.fname,new_author.lname,new_author.email,new_author.username)
        #return HttpResponse("User created successfully!")
        return redirect('home:loginuser')
    else:
        return render(req,'home/signup.html')


def loginuser(req):
    if req.method=='POST':
        user=authenticate(
            username=req.POST.get("username"),
            password=req.POST.get("password")
        )
        if user:
            login(req,user)
            return redirect('home:post')
        else:
            return HttpResponse("Access blocked,contact admin")
    else:
        return render(req,"home/login.html")
# Create your views here.

@login_required
def post(req):
    if req.method=='POST':
        new_post=Post()
        new_post.title=req.POST.get("title")
        new_post.content=req.POST.get("content")
        new_post.posted_by=req.user
        new_post.save()
        return HttpResponse("Post added successfully!")
    else:
        return render(req,'home/post.html')
    
def index(req):
    posts=Post.objects.all()
    return render(req,'home/index.html',{'posts':posts})

def post_by_user(req):
    user=User.objects.get(username=req.GET['name'])
    posts=Post.objects.filter(posted_by=user)
    return render(req,'home/index.html',{'posts':posts})

def archive_monthly(req):
    month=req.GET['month']
    year=req.GET['year']
    posts=Post.objects.filter(timestamp__month=month,timestamp__year=year)
    return render(req,'home/index.html',{'posts':posts})

def archive_yearly(req):
    year=req.GET['year']
    posts=Post.objects.filter(timestamp__year=year)
    return render(req,'home/index.html',{'posts':posts})


def post_by_id(req,post_id):
    posts=Post.objects.filter(id=post_id)
    return render(req,'home/index.html',{'posts':posts})

# def contactus(req):
#     if req.method=="POST":
#         form=contactForm(req.POST)
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             email=form.cleaned_data['email']
#             message=form.cleaned_data['message']
#             return HttpResponse("Submitted")


#     else:
#         form=contactForm()
#         return render(req,'home/contactus.html',{'form':form})


def contactus(req):

    if req.method=="POST":

        form=Contactform(req.POST)

        if form.is_valid():

            name=form.cleaned_data['name']

            email=form.cleaned_data['email']

            message=form.cleaned_data['message']

            contact_us=Contact()

            contact_us.name=req.POST.get('name')

            contact_us.email=req.POST.get('email')

            contact_us.message=req.POST.get('message')

            contact_us.save()

            print(name,email,message)

            return HttpResponse("Successful")

    else:

        form=Contactform()

        return render(req,'home/contactus.html',{'form':form})

def home_view(req):
    return render(req,'home/home_view.html')

def overview(req):
    return render(req,'home/overview.html')
    
# def posts(req):
#     return render(req,'home/posts.html')


def posts(req):
    posts=Post.objects.all()

    return render(req,'home/posts.html',{'posts':posts})

    
def insights(req):
    return render(req,'home/insights.html')
    
    