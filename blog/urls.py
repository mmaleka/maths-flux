from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from accounts.views import (
    login_view,
    register_view,
    logout_view,
    profile_view,
)
from home.views import home_view

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home_view, name="home"),
    url(r'^posts/', include('posts.url')),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^register/', register_view, name="register"),
    url(r'^profile/', profile_view, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)