from django.shortcuts import render
from posts.models import Post
# Create your views here.

def home_view(request):
    tags = Post.tag.all()
    lenTags = int(len(tags)/2)
    tags_1st = tags[:lenTags]
    tags_2nd = tags[lenTags:]
    print(lenTags)

    context={
        'tags_1st': tags_1st,
        'tags_2nd': tags_2nd
    }

    return render(request, 'posts/home.html', context)