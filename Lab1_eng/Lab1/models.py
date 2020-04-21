from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

class Message(models.Model):
    # chat = models.ForeignKey(Chat, verbose_name=_("Чат"))
    author = models.ForeignKey(User, verbose_name="Отправитель", on_delete=models.CASCADE, related_name="author_to_user" )
    recipient = models.ForeignKey(User, verbose_name='Получатель', on_delete=models.CASCADE, related_name="recipient_to_user")
    text = models.TextField("Сообщение")
    pub_date = models.DateTimeField('Дата сообщения', default=now)

    class Meta:
        ordering=['pub_date']

    def __str__(self):
        return self.text
