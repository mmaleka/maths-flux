from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from .forms import UserLoginForm
from posts.models import Post
from accounts.forms import RegistrationForm
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.




def login_view(request):
    print(request.user.is_authenticated)
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    print("request.user.is_authenticated1", request.user.is_authenticated)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print("request.user.is_authenticated2", request.user.is_authenticated)
        # Redirect here
        if next:
            return redirect(next)
        return redirect('posts:list')

    tags = Post.tag.all()
    lenTags = int(len(tags) / 2)
    tags_1st = tags[:lenTags]
    tags_2nd = tags[lenTags:]
    context = {
        "form": form,
        "title": "Login",
        'tags_1st': tags_1st,
        'tags_2nd': tags_2nd
    }

    return render(request, "posts/form.html", context)


def register_view(request):
    next = request.GET.get('next')
    tags = Post.tag.all()
    lenTags = int(len(tags) / 2)
    tags_1st = tags[:lenTags]
    tags_2nd = tags[lenTags:]
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            if next:
                return redirect(next)
            return redirect('posts:list')
    else:
        form = RegistrationForm()
        context = {
            'title': 'Sign Up',
            'form': form,
            'tags_1st': tags_1st,
            'tags_2nd': tags_2nd
        }
        return render(request, "posts/form.html", context)


def logout_view(request):
    logout(request)
    # Redirect here aswell
    return redirect('posts:list')
    #return render(request, "posts/form.html", {})



def profile_view(request):
    tags = Post.tag.all()
    lenTags = int(len(tags) / 2)

    tags_1st = tags[:lenTags]
    tags_2nd = tags[lenTags:]
    print(tags_2nd)
    context = {
        'title': 'User Profile',
        'user': request.user,
        'tags_1st': tags_1st,
        'tags_2nd': tags_2nd
    }

    return render(request, "posts/profile.html", context)























