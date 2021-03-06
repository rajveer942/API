from django.contrib import admin
from .models import StudentModelViewSet

# Register your models here.
class StudentModelViewSetAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
admin.site.register(StudentModelViewSet,StudentModelViewSetAdmin)