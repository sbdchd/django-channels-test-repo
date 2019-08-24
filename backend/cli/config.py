def setup_django():
    import os
    from dotenv import load_dotenv
    import django

    load_dotenv()
    os.environ["PYTHONUNBUFFERED"] = "true"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    django.setup(set_prefix=False)


def setup_django_sites():
    import os
    from django.conf import settings
    from django.contrib.sites.models import Site
    from allauth.socialaccount.models import SocialApp

    my_site = Site.objects.get(pk=settings.SITE_ID)
    my_site.domain = "recipeyak.com"
    my_site.name = "RecipeYak"
    my_site.save()

    oauth_providers = list(settings.SOCIALACCOUNT_PROVIDERS.keys())
    for provider in oauth_providers:
        obj, _ = SocialApp.objects.get_or_create(provider=provider)
        obj.name = provider
        obj.client_id = os.environ[f"OAUTH_{provider}_CLIENT_ID".upper()]
        obj.secret = os.environ[f"OAUTH_{provider}_SECRET".upper()]
        obj.sites.add(settings.SITE_ID)
        obj.save()


def set_default_testing_variables():
    """
    Default configuration to load for testing and linting

    load_dotenv() should be called after this to allow overriding these
    variables.
    """
    import os

    os.environ["DEBUG"] = "1"
    os.environ.setdefault("DATABASE_URL", "postgres://postgres@127.0.0.1:5432/postgres")
