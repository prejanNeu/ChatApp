from django.db import models
from django.contrib.auth.models import User



class userInfo (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField ()
    gender = models.CharField(max_length=7)


class chatRoom(models.Model):
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)


    
class message(models.Model):
    room = models.ForeignKey(chatRoom,on_delete=models.CASCADE)
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"message form {self.sender} in {self.room}"

