# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models import Q
from sorl.thumbnail import get_thumbnail


class User(AbstractUser):
    NONE = 0
    MALE = 1
    FEMALE = 2
    ALL = 3
    GENDER = {
        (NONE, u''),
        (MALE, u'Hombre'),
        (FEMALE, u'Mujer')
    }
    PREFERENCES = {
        (MALE, u'Solo chicos'),
        (FEMALE, u'Solo chicas'),
        (ALL, u'Ambos')
    }
    image = models.ImageField(
        u'Imagen',
        default='login_img.jpg',
        upload_to='users',
    )
    invited_by = models.ForeignKey('User', null=True, blank=True, verbose_name='Invitado por', related_name='user_invited_by')
    college = models.ForeignKey('Colleges', null=True, blank=True, verbose_name='Universidad')
    study = models.ForeignKey('Studies', null=True, blank=True, verbose_name='Estudios')
    points = models.IntegerField(default=0, verbose_name='Puntos')
    gender = models.IntegerField(choices=GENDER, default=NONE, verbose_name='Género')
    preference = models.IntegerField(choices=PREFERENCES, default=ALL, verbose_name='Preferencia')
    id_instagram = models.CharField(max_length=120, null=True, blank=True)
    carousel = models.ManyToManyField('User', blank=True, related_name='user_carousel')

    def register_completed(self):
        return self.college and self.study and self.gender

    def get_pixelated_image_url(self, percent_depix=0):
        size = percent_depix + 15
        if percent_depix == 100:
            size = 400
        if self.image:
            return get_thumbnail(self.image, '%sx%s' % (size, size), crop='center', quality=90).url

        return get_thumbnail('login_img.jpg', '%sx%s' % (size, size), crop='center', quality=90).url

    def get_carousel(self):
        if self.carousel.exists():

            return self.carousel.all()

        users = User.objects.filter(
            is_active=True,
            college=self.college,
            is_superuser=False
        ).exclude(
            college__isnull=True
        ).exclude(
            study__isnull=True
        ).exclude(
            gender__isnull=True
        ).exclude(
            id=self.id
        )

        # Filtramos por genero
        if self.preference != User.ALL:
            users = users.filter(gender=self.preference)

        users = users.order_by('?')[:10]
        for u in users:
            self.carousel.add(u)
        return self.carousel.all()

    def get_current_game_users(self):
        return Chat.objects.filter(
            Q(user_one=self) | Q(user_two=self)
        ).filter(percent_depix__lt=100)


class Colleges(models.Model):
    name = models.CharField(u'Nombre', max_length=100)

    class Meta:
        verbose_name = u'Universidad'
        verbose_name_plural = 'Universidades'

    # def __str__(self):
    #     return '%s' % self.name

    def __unicode__(self):
        return u'%s' % self.name


class Studies(models.Model):
    name = models.CharField(u'Nombre', max_length=100)

    class Meta:
        verbose_name = u'Estudio'

    def __unicode__(self):
        return u'%s' % self.name


class Chat(models.Model):
    """
    Tabla de chat entre usuarios
    """
    user_one = models.ForeignKey(
        User,
        related_name='chat_user_one',
        verbose_name='Usuario 1'
    )
    user_two = models.ForeignKey(
        User,
        related_name='chat_user_two',
        verbose_name='Usuario 2'
    )
    timestamp = models.DateTimeField(u'Fecha de creación', auto_now_add=True)
    timestamp_last_interaction = models.DateTimeField(u'Fecha de última interacción', null=True, blank=True)
    percent_depix = models.IntegerField(u'Porciento Depix', default=0)
    attempts = models.IntegerField(u'Intentos restantes', default=3)

    class Meta:
        unique_together = (("user_one", "user_two"),)

    def __unicode__(self):

        return u'%s - %s (Depixs: %s)' % (self.user_one.username, self.user_two.username, self.percent_depix)

    def save(self, *args, **kwargs):
        self.update_percent_depix()
        super(Chat, self).save(*args, **kwargs)

    def update_percent_depix(self):
        """
        Método para actualizar el porcentaje de despixelación de la foto.

        Forma de calcular el porcentaje:
        De los dos usuarios participantes en el chat, se cuenta cuantas interacciones mayores de 10 carácteres
        a realizado cada usuario y quien tengo menos se divide entre el número *settings.NUM_CONVERSATION_TO_DIVIDE_FOR_PERCENT*
        que será el número para llegar al 100%. En caso de tener el 100% no se realiza ningún cálculo.

        Ejemplo:
            - variable NUM_CONVERSATION_TO_DIVIDE... = 50
            - Usuario 1: 15 interacciones
            - Usuario 2: 50 interacciones
            - 15 / 50 = 0.3
            - 0.3 * 100 = 30%
            - Foto despixelada un 30%

        :return: nothing
        """
        n_interactions_user_one = self.interaction_set.filter(author=self.user_one, message_len__gt=settings.MIN_CHARACTERS_TO_DEPIXS).count()
        n_interactions_user_two = self.interaction_set.filter(author=self.user_two, message_len__gt=settings.MIN_CHARACTERS_TO_DEPIXS).count()

        if self.percent_depix >= 100:
            return

        smaller = n_interactions_user_one if n_interactions_user_one < n_interactions_user_two else n_interactions_user_two

        if smaller == 0:
            return

        percent = smaller / settings.NUM_CONVERSATION_TO_DIVIDE_FOR_PERCENT
        # Aumentan los puntos del usuario B
        self.user_two.points += 10

        if percent > 1:
            percent = 1
        self.percent_depix = 100 * percent

    def get_end_time(self):
        return self.timestamp + datetime.timedelta(hours=24)

    def hours_remaining(self):
        return (self.timestamp + datetime.timedelta(hours=24) - datetime.datetime.now()).seconds//3600

    def last_interaction(self):
        return self.interaction_set.first()

    def get_pixelated_image_url(self):
        return self.user_two.get_pixelated_image_url(self.percent_depix)


class Interaction(models.Model):
    """
    Interacción de un chat
    """
    chat = models.ForeignKey(Chat)
    author = models.ForeignKey(User, verbose_name='Autor')
    message = models.TextField('Mensaje')
    message_len = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(u'Fecha de envío', auto_now_add=True)
    unread = models.BooleanField('Sin leer', default=True)

    class Meta:
        verbose_name = u'Interacción'
        verbose_name_plural = 'Interacciones'
        ordering = ('-timestamp',)

    def save(self, *args, **kwargs):
        self.message_len = len(self.message)
        super(Interaction, self).save(*args, **kwargs)
        self.chat.timestamp_last_interaction = self.timestamp
        self.chat.save()

    def __unicode__(self):
        return u'%s - %s' % (self.author, self.message)
