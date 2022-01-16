from django.contrib import admin

# Register your models here.
from .models import Message, SuvMessage, TmpUser

admin.site.register(Message)
admin.site.register(SuvMessage)
admin.site.register(TmpUser)