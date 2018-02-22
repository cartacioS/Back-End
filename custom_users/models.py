from django.contrib.auth.models import AbstractUser
from rest_framework_jwt.settings import api_settings
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)

    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save(*args, **kwargs)

    @property
    def token(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(self)
        payload['full_name'] = self.get_full_name()
        token = jwt_encode_handler(payload)
        return token
