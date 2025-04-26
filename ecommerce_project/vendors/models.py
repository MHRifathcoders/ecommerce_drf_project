from django.db import models
from users.models import User

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    shop_name = models.CharField(max_length=255)

    def __str__(self):
        return self.shop_name
