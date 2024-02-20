from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ReviewModel)
admin.site.register(CartModel)
admin.site.register(OwnedCoursesModel)
admin.site.register(WishlistModel)