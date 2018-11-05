from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class UserlikeManager(models.Manager):
    def get_all_mutal_likes(self, user):
        qs = user.liker.liked_users.all()
        mutual_users = []
        for liked_user in qs:
            try:
                if other_user.liker.get_all_mutal_like(user):
                    mutual_users.append(other_user)
            except:
                pass
        return mutual_users

class UserLike(models.Model):
    user = models.OneToOneField(User, related_name='Liker',on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(User, related_name='liked_users', blank=True)

    objects = UserlikeManager()

    def __str__(self):
        return self.user.username

    def get_mutual_like(self, user_b):
        i_like = False
        you_like = False
        if user_b in self.liked_users.all():
            i_like = True
        liked_user, created = UserLike.objects.get_or_create(user=user_b)
        if self.user in liked_user.liked_users.all():
            you_like = True
        if you_like and i_like:
            return True
        else:
            return False