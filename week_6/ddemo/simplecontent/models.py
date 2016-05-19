from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=128)
    article_text = models.TextField(null=False, blank=False)
    current = models.BooleanField(null=False, default=True, db_index=True)
    slug = models.SlugField(null=False, db_index=True)
    views = models.PositiveIntegerField(null=False, default=0)
    authors = models.ManyToManyField(User)
    publish_date = models.DateTimeField(auto_now_add=True, db_index=True)
    cover_photo = models.OneToOneField('Photo', null=True, related_name='cover_photo')
    photos = models.ManyToManyField('Photo')

    created = models.DateTimeField(auto_now_add=True)
    modefied = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ": " + self.title

class Comment(models.Model):
    comment_text = models.TextField(max_length=2000, blank=False)
    moderated = models.BooleanField(default=False, null=False)
    likes = models.PositiveIntegerField(default=0, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modefied = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Photo(models.Model):
    image = models.ImageField()
    photographer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    caption = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id)
