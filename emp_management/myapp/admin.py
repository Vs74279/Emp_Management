from django.contrib import admin
from myapp.models import Emp



class EmpAdmin(admin.ModelAdmin):
    list_display=('name','phone','working','department')
    search_fields=('name','department')
# Register your models here.
admin.site.register(Emp,EmpAdmin)