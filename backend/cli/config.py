def setup_django():
    import os
    import django

    os.environ["PYTHONUNBUFFERED"] = "true"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    django.setup(set_prefix=False)


def set_default_testing_variables():
    """
    Default configuration to load for testing and linting

    load_dotenv() should be called after this to allow overriding these
    variables.
    """
    import os

    os.environ["DEBUG"] = "1"
    os.environ.setdefault("DATABASE_URL", "postgres://postgres@127.0.0.1:5432/postgres")
