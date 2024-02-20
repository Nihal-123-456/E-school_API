from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ROLE={
    ('teacher','teacher'),
    ('student','student'),
}

class UserInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, choices=ROLE)
    image = models.ImageField(upload_to='user/image/')