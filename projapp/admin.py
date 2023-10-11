from django.contrib import admin
from projapp.models import contactm

# Register your models here.
class contactmAdmin (admin.ModelAdmin):
	list_display=['eno','ename','esal','eaddr']

admin.site.register(contactm, contactmAdmin)   
