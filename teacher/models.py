from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TopicModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CourseModel (models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='teacher/image/')
    title = models.CharField(max_length=100)
    topics = models.ManyToManyField(TopicModel)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title