# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from random import choice
from string import ascii_uppercase

from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from push_notifications.models import GCMDevice, APNSDevice

from core.models import *
from django.conf import settings


def login(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect(reverse('home'))

    context = {
        'data': request.POST,
    }
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            context.update({'error_msg': u'Usuario y/o contraseña inválido/s.'})

    return render(request, 'login.html', context)


def register(request):
    auth_logout(request)
    context = {}

    colleges = Colleges.objects.all()
    studies = Studies.objects.all()

    context.update({
        'colleges': colleges,
        'studies': studies
    })

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        study = request.POST.get('study')
        college = request.POST.get('college')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')

        try:
            user = User.objects.create(
                username=username,
                email=email,
                gender=gender
            )
            if image:
                user.image = image

            user.study_id = study
            user.college_id = college
            user.points = 250

            user.set_password(password)
            user.save()
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        except IntegrityError:
            context.update({
                    'error_msg': u'Ya existe un usuario con esa dirección email.',
                    'data': request.POST
                })

    return render(request, 'register.html', context)


def password_recovery(request):
    context = {}
    if 'email' in request.POST:
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = (''.join(choice(ascii_uppercase) for i in range(8)))
            user.set_password(new_password)
            user.save()
            print new_password
            context.update({'success_msg': u'Se ha enviado una contraseña nueva al email indicado.'})
            message = u'Tu nueva contraseña de acceso a Depixs es: %s' % new_password
            send_mail('Depixs: Recuperacion de contraseña', message, 'noreply@depixs.com', (email,))
        except User.DoesNotExist:
            context.update({'error_msg': u'No existe ningún usuario con esa dirección email.'})

    return render(request, 'password_recovery.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("login"))


@login_required
def home(request):
    context = {
        'section': 'home',
    }
    if request.POST:
        for user_two in request.user.get_carousel().order_by('?'):

            if not Chat.objects.filter(user_two=request.user, user_one=user_two).exists() and not Chat.objects.filter(
                    user_two=user_two, user_one=request.user).exists():

                chat, created = Chat.objects.get_or_create(
                    user_one=request.user,
                    user_two=user_two,
                )
                if created:
                    push_notifications(
                        request, user_two, u'¡Empieza el juego!',
                        u'%s va a intentar despixelarte, ayúdale a hacerlo' % request.user.username,
                        '/chats/%s/' % chat.id
                    )

                    url = reverse('chat', kwargs={'pk': chat.id})
                    return HttpResponseRedirect(url)

        context.update({'empty': True})

    return render(request, 'carousel.html', context)


@login_required
def ranking(request):
    users = User.objects.filter(
        is_active=True,
    ).order_by('-points')

    if request.GET.get('username'):
        users = users.filter(username__icontains=request.GET.get('username'))

    if request.GET.get('study'):
        users = users.filter(study_id=request.GET.get('study'))

    if request.GET.get('college'):
        users = users.filter(college_id=request.GET.get('college'))

    colleges = Colleges.objects.all()
    studies = Studies.objects.all()

    context = {
        'section': 'ranking',
        'users': users[:100],
        'colleges': colleges,
        'studies': studies,
        'filters': request.GET
    }

    return render(request, 'ranking.html', context)


@login_required
def config(request):
    context = {
        'section': 'config',
    }

    return render(request, 'config.html', context)


@login_required
def user_profile(request):
    context = {
        'section': 'config',
        'sub_menu_settings': True
    }

    colleges = Colleges.objects.all()
    studies = Studies.objects.all()

    if request.POST:
        request.user.study_id = request.POST.get('study')

        if request.FILES:
            request.user.image = request.FILES.get('image')
        if int(request.POST.get('college')) != request.user.college_id or int(
                request.POST.get('preference')) != request.user.preference:
            if not request.user.get_current_game_users():
                request.user.college_id = request.POST.get('college')
                request.user.preference = request.POST.get('preference')

            else:
                context.update({
                    'error_msg': 'No puedes cambiar tu universidad ni tu preferencia si tienes juegos activos.'
                })

        request.user.save()

    user = User.objects.get(pk=request.user.pk)

    context.update({
        'colleges': colleges,
        'studies': studies,
        'user': user
    })

    return render(request, 'settings_components/user_profile.html', context)


@login_required
def chats(request):

    chats = Chat.objects.filter(
        Q(user_one=request.user) | Q(user_two=request.user)
    ).order_by('-timestamp_last_interaction')

    context = {
        'section': 'chats',
        'chats': chats,
        'games': request.user.get_current_game_users(),
        'filters': request.GET,
    }

    return render(request, 'chats.html', context)


@login_required
def interactions(request, pk):
    chat = Chat.objects.get(pk=pk)

    if request.POST:
        Interaction.objects.create(
            chat=chat,
            author=request.user,
            message=request.POST['message'],
        )

        user = chat.user_one

        if request.user.pk == chat.user_two_id:
            user = chat.user_two
        push_notifications(request, user, request.user.username, request.POST['message'], '/chats/%s/' % chat.id)

    chat_interactions = chat.interaction_set.all()
    if request.GET.get('from'):
        chat_interactions = chat_interactions.filter(pk__gt=request.GET['from'])

    if request.POST.get('from'):
        chat_interactions = chat_interactions.filter(pk__gt=request.POST['from'])

    chat_interactions = chat_interactions[:25]

    interactions = []
    for interaction in chat_interactions:
        interactions.append({
            'pk': interaction.pk,
            'author': interaction.author_id,
            'message': interaction.message,
        })
    chat.refresh_from_db()
    return JsonResponse({
        'interactions': list(reversed(interactions)),
        'percent_depix': chat.percent_depix,
        'pixelated_image_url': chat.get_pixelated_image_url()
    })


@login_required
def chat(request, pk):
    chat = Chat.objects.get(pk=pk)

    context = {
        'section': 'chat_room',
        'sub_menu_chat': True,
        'chat': chat,
        'user2_image': chat.user_two.image,
        'user2_username': chat.user_two.username,
    }

    if request.POST:

        user_checked = request.POST.get('check')
        correct_user = chat.user_two.username

        if user_checked == correct_user:

            push_notifications(
                request, chat.user_two, u'¡Te han despixelado!',
                u'%s ha conseguido despixelarte, se conservará el chat entre ambos.' % chat.user_one.username,
                '/chats/'
            )

            # OLD
            # chat_percent = int(chat.percent_depix)
            # earned_points = 0

            # if chat_percent < 100:
            #
            #     percent_depix = chat_percent / 100
            #     earned_points = chat.user_two.points * percent_depix
            #     earned_points_rounded = round(earned_points, 0)
            #
            #     chat.user_one.points += earned_points_rounded
            #
            #     # Le damos el 100% de depixs al final para que deje de ser un juego y pase a ser un chat
            #     chat.percent_depix = 100
            #
            # elif chat_percent == 100:
            #     earned_points = chat.user_two.points
            #     chat.user_one.points += earned_points

            # NEW
            # Le damos el 100% de depixs al final para que deje de ser un juego y pase a ser un chat
            chat.percent_depix = 100
            chat.user_one.points += settings.POINTS_WIN_DEPIXS

            chat.user_one.save()
            chat.save()

            context.update({
                'winner': 'winner',
                'earned_points': settings.POINTS_WIN_DEPIXS,
                'total_points': chat.user_one.points
            })

        else:
            # NEW
            chat.user_one.points -= settings.POINTS_LOSE_DEPIXS

            if chat.user_one.points < 0:
                chat.user_one.points = 0

            chat.user_one.save()

            context.update({
                'attempt': 'attempt',
                'points_lost': settings.POINTS_LOSE_DEPIXS
            })

            return render(request, 'chat.html', context)

            # OLD
            # attempts_left = int(request.POST.get('attempts'))
            # attempts_left -= 1
            #
            # if attempts_left == 0:
            #
            #     push_notifications(
            #         request, chat.user_two, u'¡Oooh!',
            #         u'%s no ha conseguido despixelarte, se ha perdido el chat.' % chat.user_one.username,
            #         '/home/'
            #     )
            #     chat.delete()
            #
            #     context.update({
            #         'loser': 'loser'
            #     })
            #
            # else:
            #     chat.attempts = attempts_left
            #     chat.save()
            #
            #     context.update({
            #         'attempt': 'attempt'
            #     })
            #
            #     return render(request, 'chat.html', context)

    return render(request, 'chat.html', context)


@login_required
def terms_and_conditions(request):
    context = {
        'section': 'config',
        'sub_menu_settings': True
    }

    return render(request, 'settings_components/terms_and_conditions.html', context)


@login_required
def push_notifications(request, user, title, message, url):
    GCMDevice.objects.filter(
        active=True,
        user=user
    ).send_message(None, extra={
        'm_title': title,
        'm_message': message,
        'url': url
    })

    for APN in APNSDevice.objects.filter(
            active=True,
            user=user):
        APN.send_message(message={
            'title': title,
            'body': message,
            'url': url
        },
            sound='default'
        )
