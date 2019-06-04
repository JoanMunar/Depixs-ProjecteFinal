# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from push_notifications.models import GCMDevice, APNSDevice

from core.models import User


class Command(BaseCommand):
    help = u'Notificaciones depixs'

    def handle(self, *args, **options):

        hours = 3

        users = User.objects.filter(
            is_active=True,
        )

        for user in users:
            games = user.get_current_game_users()

            for game in games:

                hours_remaining = int(game.hours_remaining())
                title = ''
                message = ''
                url = ''

                if hours_remaining == hours:
                    title = u'¡Se termina el tiempo!'
                    message = u'Faltan %s horas para que finalice el juego con %s' % (hours, game.user_two)
                    url = '/chats/%s/' % game.id
                elif hours_remaining == 0:

                    date = game.timestamp.date()
                    date_parsed = date.strftime("%d/%m/%Y")
                    hour = game.timestamp.time()
                    hour_parsed = hour.strftime("%H:%M")

                    title = u'¡El juego ha finalizado!'
                    message = u'El juego iniciado el %s a las %s ha finalizado' % (date_parsed, hour_parsed)
                    url = '/home/'

                GCMDevice.objects.filter(
                    active=True,
                    user=game.user_one_id if game.user_two_id == user.pk else game.user_two_id
                ).send_message(None, extra={
                    'm_title': title,
                    'm_message': message,
                    'url': url
                })

                for APN in APNSDevice.objects.filter(
                        active=True, user=game.user_one_id if game.user_two_id == user.pk else game.user_two_id):
                    APN.send_message(message={
                        'title': title,
                        'body': message,
                        'url': url
                    },
                        sound='default'
                    )
