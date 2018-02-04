from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from taggit.managers import TaggableManager


from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys



# Create your models here.
from comments.models import Comment


def upload_location(instance, filename):
    return "%s/%s" %(instance.user, filename)

class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, blank=True,
                              height_field="height_field",
                              width_field="width_field")
    height_field=models.IntegerField(null=True, default=0)
    width_field = models.IntegerField(null=True, default=0)
    content=models.TextField()
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    # tag = models.CharField(null=True, max_length=50)
    tag = TaggableManager()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    def get_tag_url(self):
        return '/posts/tag/{}'.format(self.id)

    class Meta:
        ordering = ['-timestamp']

    @property
    def get_content_type(self):
        instance = self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slug(instance, new_slug=None):
    slug= slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs=Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_reicever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)


pre_save.connect(pre_save_post_reicever, sender=Post)