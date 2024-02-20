from django.contrib import admin
from .models import *

# Register your models here.
class TopicAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug':['name',]}

admin.site.register(TopicModel, TopicAdmin)
admin.site.register(CourseModel)