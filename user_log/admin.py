from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(College)
admin.site.register(MainEvent)
admin.site.register(SubEvents)
admin.site.register(Games)