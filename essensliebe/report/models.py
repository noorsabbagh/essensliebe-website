from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.urls import reverse

# Create your models here.
user_obj = User.objects.get(username='admin')

QUEST = (
		('This person is annoying me', 'This person is annoying me'), 
		('They are pretending to be me or someone i know', 'They are pretending to be me or someone i know'),
		('They are sharing inappropriate or offensive message', 'They are sharing inappropriate or offensive message'),
		('This is a fake account', 'This is a fake account'),
        ('This profile represents a business or organization', 'This profile represents a business or organization'),
        ('They are using a different name than they use in everday life', 'They are using a different name than they use in everday life'),
		('other', 'other'),
        )


class UserReport(models.Model):
    report_category = models.CharField(max_length=100, choices=QUEST)
    reason_for_report = models.CharField(max_length=3000)
    report_url = models.CharField(max_length=3000)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_repot', null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='recived_report', null=True, blank=True)
    sent = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_report', null=True, blank=True)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return self.report_category

