from django.db import models


class PostViews(models.Model):
    CONTENT_TYPES = [
        ('question', 'question'),
        ('article', 'article'),
    ]

    ip_address = models.GenericIPAddressField(default="0.0.0.0")
    created_date = models.DateTimeField(auto_created=True, null=True, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.ip_address} in {self.post.title} post'
