from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Blog(models.Model):
      title = models.CharField(max_length=100, null=False,  default = "")
      content = models.TextField(null=False, default = "")
      publish_date = models.DateTimeField(null=False, default= datetime.now)
      author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)