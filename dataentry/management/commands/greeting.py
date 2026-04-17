from django.core.management.base import BaseCommand

# Proposed command = python manage.py greeting (name whom to greet)
# Proposed output = Hi {name}, Good Morning
class Command(BaseCommand):
    help = "Greets the user"


    def add_arguments(self, parser):  # parser allow to write extra after command
        parser.add_argument('name', type=str, help='Specifies user name')

    def handle(self, *args, **kwargs):
        # write the logic
        name = kwargs['name']
        greeting = f"Hi {name}, Good Morning"
        self.stderr.write(greeting) # it show error
        self.stdout.write(self.style.SUCCESS(greeting)) # this way you can give error, warning