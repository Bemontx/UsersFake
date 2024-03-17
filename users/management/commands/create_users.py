from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

Usuario = get_user_model()

class Command(BaseCommand):
    help = 'Genera usuarios falsos masivamente'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(100):
            username = fake.user_name()
            email = fake.email()
            if not Usuario.objects.filter(username=username).exists() and not Usuario.objects.filter(email=email).exists():
                Usuario.objects.create(username=username, email=email)
