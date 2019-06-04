from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.landing, name='landing'),
    url(r'^$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^recover-password/$', views.password_recovery, name='password_recovery'),
    url(r'^home/$', views.home, name='home'),
    url(r'^chats/$', views.chats, name='chats'),
    url(r'^chats/(?P<pk>\d+)/$', views.chat, name='chat'),
    url(r'^chats/(?P<pk>\d+)/interactions/$', views.interactions, name='interactions'),
    url(r'^ranking/$', views.ranking, name='ranking'),
    url(r'^config/user-profile/$', views.user_profile, name='user_profile'),
    url(r'^config/terms-and-conditions/$', views.terms_and_conditions, name='terms_and_conditions'),
    url(r'^config/$', views.config, name='config'),
    url(r'^logout/$', views.logout, name='logout'),

]
