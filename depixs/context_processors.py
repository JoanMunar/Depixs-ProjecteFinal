from django.conf import settings # import the settings file


def general_context(request):

    general = {
        'media_version': getattr(settings, 'MEDIA_VERSION', ''),
        }

    return general


