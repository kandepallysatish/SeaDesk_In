from django.db import models

# Create your models here.

# LOGIN, LOGOUT, REGISTER
from django.db import models
from django.contrib.auth.models import User


class Animesview(models.Model):
    post_id = models.AutoField(primary_key=True)
    name_episode = models.CharField(max_length=50, default="")
    language = models.CharField(max_length=50)
    year = models.IntegerField()
    thumbnail = models.CharField(max_length=5000, default="")
    video = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.name_episode


class Jobupdatesview(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="")
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    chead1 = models.CharField(max_length=5000, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.CharField(max_length=5000, default="")

    def __str__(self):
        return str(self.post_id)


class Contactus(models.Model):
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    email = models.CharField(max_length=120)
    number = models.IntegerField(blank=True)
    desc = models.TextField()

    def __str__(self):
        return str(self.post_id)


class Question(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_responses(self):
        return self.responses.filter(parent=None)

class Response(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE, related_name='responses')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    def get_responses(self):
        return Response.objects.filter(parent=self)