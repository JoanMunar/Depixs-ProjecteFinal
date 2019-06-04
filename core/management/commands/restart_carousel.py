
from django.core.management.base import BaseCommand

from core.models import User


class Command(BaseCommand):

    help = 'Reinicia el carousel si no tienes juegos activos'

    def handle(self, *args, **options):

        users = User.objects.filter(
            is_active=True,
        )

        for user in users:

            games = user.get_current_game_users()

            if not games:
                user.carousel.clear()
