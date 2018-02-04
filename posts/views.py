from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from .models import Post
from .forms import PostForm
from comments.forms import CommentForm
from django.views.generic import DetailView, ListView




@login_required(login_url="/login")
def post_create(request): # Create post (PUT)
    if not request.user.is_authenticated:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        print(form.cleaned_data)
        # Will put message saying success
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, "Not successfully created")
    tags = Post.tag.all()
    lenTags = int(len(tags)/2)
    tags_1st = tags[:lenTags]
    tags_2nd = tags[lenTags:]
    context = {
        'title': 'Ask A Question',
        "form": form,
        'tags_1st': tags_1st,
        'tags_2nd': tags_2nd
    }
    return render(request, "posts/post_form.html", context)



def post_detail(request, id): # Retrive post (GET)
    instance=get_object_or_404(Post, id=id)

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id,
    }

    form = CommentForm(request.POST or None, request.FILES or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated:
        print(form.cleaned_data)
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        model_pic = form.cleaned_data.get("image")
        new_comment, created = Comment.objects.get_or_create(
            user = request.user,
            content_type=content_type,
            object_id = obj_id,
            content=content_data,
            model_pic=model_pic,
        )

        if created:
            print("yeah")


    content_type=ContentType.objects.get_for_model(Post)
    obj_id=instance.id
    comments=Comment.objects.filter(content_type=content_type, object_id=obj_id)
    tags = Post.tag.all()
    lenTags = int(len(tags)/2)
    tags_1st = tags[:lenTags]
    tags_2nd = tags[lenTags:]
    context={
        'title': instance.title,
        'instance': instance,
        'comments': comments,
        'comment_form': form,
        'tags_1st': tags_1st,
        'tags_2nd': tags_2nd,
    }
    return render(request, "posts/post_detail.html", context)


def post_list(request): # Retrive post (GET)
    queryset_list = Post.objects.all().order_by("-timestamp")
    # print("queryset_list: ", len(queryset_list))
    query = request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)


    tags = Post.tag.all()
    print(tags)
    lenTags = int(len(tags)/2)
    tags_1st = tags[:lenTags]
    tags_2nd = tags[lenTags:]
    context={
        'title': 'List',
        'object_list': queryset,
        'queryset_list': len(queryset_list),
        'tags_1st': tags_1st,
        'tags_2nd': tags_2nd
    }

    return render(request, "posts/index.html", context)



def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # Will put message saying success
        messages.success(request, "Successfully updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    return render(request, "posts/post_form.html", context)


def post_delete(request, id=None):
    if not request.user.is_authenticated:
        raise Http404

    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect('posts:list')


def TagIndexView(request, slug):
    print(slug)

    queryset_list = Post.objects.filter(tag__slug=(slug)).order_by("-timestamp")
    print(queryset_list)
    tags = Post.tag.all()
    lenTags = int(len(tags)/2)
    tags_1st = tags[:lenTags]
    tags_2nd = tags[lenTags:]
    context = {
        'title': 'List',
        'object_list': queryset_list,
        'queryset_list': len(queryset_list),
        'tags_1st': tags_1st,
        'tags_2nd': tags_2nd
    }

    return render(request, "posts/index.html", context)

