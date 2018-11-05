from django.contrib import admin
from .models import UserReport

# Register your models here.

class UserReportAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id"]
    class Meta:
        model = UserReport

admin.site.register(UserReport, UserReportAdmin)


