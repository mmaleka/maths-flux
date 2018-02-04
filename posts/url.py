from django.conf.urls import url
from posts import views

app_name = 'posts'
urlpatterns = [
    url(r'^$', views.post_list, name="list"),
    url(r'^create/$', views.post_create, name="post_create"),
    url(r'^(?P<id>\d+)/$', views.post_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name="update"),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name="post_delete"),

    # Tags urls
    # url(r'^tags/$', views.tag_list, name="tags_list"),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.TagIndexView, name="tagged"),
]