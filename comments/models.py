from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

# Create your models here.


class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    model_pic = models.ImageField(null=True, blank=True)


    def __str__(self):
        return str(self.user.username)