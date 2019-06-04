# -*- coding: utf-8 -*-
import uuid
from random import randint

from django.core.management.base import BaseCommand
from core.models import User, Colleges, Studies


class Command(BaseCommand):

    #     help = u'Recordatorio de cumpleaños x días antes'
    #
    def handle(self, *args, **options):
        for i in range(100):
            name = str(uuid.uuid4())[:10]
            User.objects.create(
                username=name,
                first_name=name,
                college=Colleges.objects.all().order_by('?')[0],
                study=Studies.objects.all().order_by('?')[0],
                points=randint(0, 1000),
                preference=randint(1, 3),
                gender=randint(1, 2)
            )

#         today = datetime.date.today()
#         message = u'cumple años dentro de 10 días.'
#
#         birthday_date = (today + datetime.timedelta(days=10))
#         for user in User.objects.filter(
#                 birthday__day=birthday_date.day,
#                 birthday__month=birthday_date.month,
#         ).exclude(is_superuser=True):
#             friends = Friendship.objects.filter(
#                 is_confirmed=True).filter(
#                 Q(user_one=user) | Q(user_two=user)
#             ).distinct()
#             for friend in friends:
#                 Notification.objects.create(
#                     author=user,
#                     recipient_id=friend.user_one_id if friend.user_two_id == user.pk else friend.user_two_id,
#                     content=message,
#                     type=2,
#                 )
