import uuid
from users.models import Profile
from django.db import models

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL,)
    Title = models.CharField(max_length=101,null=True,blank=True)
    featured_image = models.ImageField(null=True,blank=True, default="default.jpg")
    description = models.TextField(null=True, blank=True)  # null for database issuing, blank to tell Django
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, editable=False)
    vote_ratio = models.IntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # default=uuid.uuid4 -  This parameter generates more complex keys to avoid merge conflicts
    def __str__(self):
        return str(self.Title)
    @ property
    def imageURL(self):
        try:
         img = self.featured_image.url
        except:
            img = ''
        return img
class Review(models.Model):
    VOTE_TYPE = (("UP","UP"),
             ("DOWN","DOWN")
            )
    # owner
    project = models.ForeignKey(Project,on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name