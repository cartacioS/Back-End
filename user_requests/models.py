from django.db import models
from custom_users.models import User

# Create your models here.

class UserRequests(models.Model):
    groupon_url = models.URLField()
    title = models.TextField()
    poster = models.ForeignKey('custom_users.User', on_delete = models.CASCADE,)
    expiration_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now = True)
    is_fulfilled = models.BooleanField(default = False)
    group_size = models.PositiveIntegerField()
    members_needed = models.PositiveIntegerField()
    description = models.TextField()

    
