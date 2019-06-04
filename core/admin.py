# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User
from .models import Colleges
from .models import Studies
from .models import Chat
from .models import Interaction

admin.site.site_header = u'Administración de Depixs'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'college', 'study', 'points', 'gender', 'preference', 'invited_by', 'id_instagram')


admin.site.register(User, UserAdmin)

# class CollegesAdmin(admin.ModelAdmin):
# list_display = ('name',)


admin.site.register(Colleges)
admin.site.register(Studies)


class ChatAdmin(admin.ModelAdmin):
    list_display = ('user_one', 'user_two', 'timestamp', 'timestamp_last_interaction', 'percent_depix', 'attempts')


admin.site.register(Chat, ChatAdmin)


class InteractionAdmin(admin.ModelAdmin):
    list_display = ('chat', 'author', 'message', 'message_len', 'timestamp', 'unread')


admin.site.register(Interaction, InteractionAdmin)
