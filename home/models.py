import random
import string
import uuid

from django.contrib.auth.models import User
from django.db import models


def generate_random_id():
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(6))

STREAM_CHOICES = (
    ('BLOGGING', 'blogging'),
    ('LOGS', 'Daily Logs'),
)


def token_default():
    return uuid.uuid4().hex


class Hacker(models.Model):

    user = models.OneToOneField(User)
    avatar_url = models.TextField(blank=True)
    github = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    token = models.SlugField(max_length=40, default=token_default, unique=True)


class Blog(models.Model):

    def __unicode__(self):
        return self.feed_url

    user = models.ForeignKey(User)
    url = models.URLField()
    feed_url = models.URLField()
    last_crawled = models.DateTimeField('last crawled', blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True)
    stream = models.CharField(max_length=100, default=STREAM_CHOICES[0][0], choices=STREAM_CHOICES)


class Post(models.Model):

    def __unicode__(self):
        return self.title

    blog = models.ForeignKey(Blog)
    url = models.TextField()
    title = models.TextField(blank=True)
    content = models.TextField()
    date_posted_or_crawled = models.DateTimeField('date updated')
    slug = models.CharField(max_length=6, default=generate_random_id, unique=True)


class LogEntry(models.Model):

    def __unicode__(self):
        return "%s %s" % (self.date, self.post)

    post = models.ForeignKey(Post)

    date = models.DateTimeField()
    referer = models.URLField(blank=True, null=True)
    remote_addr = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
