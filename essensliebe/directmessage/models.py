from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.urls import reverse

user_obj = User.objects.get(username='admin')

class DirectMessageManager(models.Manager):
    def get_num_unread_message(self, user):
        return super(DirectMessageManager, self).filter(read=False).filter(receiver=user).count()



# Create your models here.

class DirectMessage(models.Model):
    subject = models.CharField(max_length=150)
    body = models.CharField(max_length=3000)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_direct_message', null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='recived_direct_message', null=True, blank=True)
    sent = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_message', null=True, blank=True)
    replied = models.BooleanField(default=False)
    def __str__(self):
        return self.subject
    objects = DirectMessageManager()

    def get_obsolute_url(self):
        return (reverse('view_direct_message', kwargs={'dm_id': self.id } ))

    class Meta:
        ordering = ['-sent']
def set_message_in_session(sender, user, request, **kwargs):
    direct_message = DirectMessage.objects.get_num_unread_message(user)
    request.session['num_of_message']= direct_message

user_logged_in.connect(set_message_in_session)