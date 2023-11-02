from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@my.post',
            first_name='Admin',
            last_name='I_am',
            is_superuser=True,
            is_staff=True,
            is_email_active=True
        )

        user.set_password('password')
        user.save()
