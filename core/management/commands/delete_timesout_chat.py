# -*- coding: utf-8 -*-
import datetime

from django.core.management.base import BaseCommand

from core.models import Chat


class Command(BaseCommand):

    help = 'Elimina el chat cuando el contador llega a 0.'

    def handle(self, *args, **options):

        chats = Chat.objects.all()

        for chat in chats:

            end_time = chat.get_end_time()
            print end_time

            current_time = datetime.datetime.now()
            print(current_time)

            if end_time < current_time:
                chat.delete()
            else:
                pass
