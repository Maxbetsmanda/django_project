from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User

class MessageManager(models.Manager):
    def send(self, message, user_from, user_to):
        print message, user_from, user_to
        
        if len(message) < 1:
            return False, ["Message must be 1 character or more."] 
        
        else:
            message = Message.messageManager.create(message=message, user_from_id=user_from, user_to_id=user_to)
        return True, message



class Message(models.Model):
    message = models.TextField(max_length=1000)
    user_from = models.ForeignKey(User, related_name="from_user")
    user_to = models.ForeignKey(User, related_name="to_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    messageManager = MessageManager()

    def __repr__(self):
        return "Message: {} {} {}>".format(self.message, self.user_from.username, self.user_to.username)