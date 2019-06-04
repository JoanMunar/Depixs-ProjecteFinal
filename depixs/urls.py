from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
]

if settings.DEBUG:
    from django.views.static import serve
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns = [
                      url(r'^media/(?P<path>.*)$', serve,
                          {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                  ] + staticfiles_urlpatterns() + urlpatterns

