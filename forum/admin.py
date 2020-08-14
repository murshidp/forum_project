from django.contrib import admin
from .models import Forum,Subforum,Thread

# Register your models here.
admin.site.register(Forum)
admin.site.register(Subforum)
admin.site.register(Thread)