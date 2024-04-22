from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CommentForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.

@login_required(login_url='/admin/login/')
def home(request):
    posts = Post.objects.filter(BlogCategory__name="Featured")
    AllPosts = Post.objects.all()[0:6]
    context = {
        "posts": posts,
        "AllPosts": AllPosts
    }
    return render(request, 'home.html', context)

@login_required(login_url='/admin/login/')
def post(request, pk):
    SinglePost = Post.objects.get(pk=pk)
    Relatedposts = Post.objects.filter(BlogCategory__name="Featured").exclude(pk=pk)

    context = {
        "post": SinglePost,
        "Rpost": Relatedposts,
       
    }
    return render(request, 'post.html', context)

@login_required(login_url='/admin/login/')
def author(request, username):
    # Retrieve the user object based on the username, or return 404 if not found
    user = get_object_or_404(CustomUser, username=username)

    # Filter posts by the author (user)
    user_posts = Post.objects.filter(author=user)

    context = {
        "username": username,
        "posts": user_posts
    }
    return render(request, 'author.html', context)




def logout(request):
    auth_logout(request)
    return redirect(reverse('admin:login'))



@login_required(login_url='/admin/login/')
def comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all()  # Fetch all comments related to the post

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'post.html', {'form': form, 'post': post, 'comments': comments})


# def AllComments(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments.all()
#     return render(request, 'post.html', {'comments': comments})