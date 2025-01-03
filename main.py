import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
application = get_wsgi_application()

if __name__ == "__main__":
    django.setup()
    execute_from_command_line(['manage.py', 'runserver', '8080'])