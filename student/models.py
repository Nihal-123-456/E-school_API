from django.db import models
from django.contrib.auth.models import User
from teacher.models import CourseModel

# Create your models here.
class OwnedCoursesModel (models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

class WishlistModel (models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

class CartModel (models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

class ReviewModel (models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True)