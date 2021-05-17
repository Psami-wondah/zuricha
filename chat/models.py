from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_by = models.ForeignKey(User, related_name='room', on_delete=models.CASCADE)
    def clean(self):
        if self.name:
            self.name = self.name.replace(' ', '')
    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='message', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_messages(self):
        return reversed(Message.objects.order_by('-timestamp'))