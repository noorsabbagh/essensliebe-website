from django.contrib import admin
from .models import DirectMessage
# Register your models here.

class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id"]
    class Meta:
        model = DirectMessage

admin.site.register(DirectMessage, DirectMessageAdmin)