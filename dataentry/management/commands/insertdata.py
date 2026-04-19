# I want to add some data to database using the custom command

from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = "It will insert data to the database"

    def handle(self, *args, **options):
        # logic goes here

        dataset = [
            {'roll_no': 15, 'name': 'Amit', 'age': 22},
            {'roll_no': 29, 'name': 'Sayan', 'age': 22},
            {'roll_no': 30, 'name': 'Tanmay', 'age': 22},
            {'roll_no': 50, 'name': 'Saikat', 'age': 22},
            {'roll_no': 8, 'name': 'Sayandip', 'age': 22},
            {'roll_no': 7, 'name': 'Akash', 'age': 22},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no = roll_no).exists()
            if not existing_record:
                Student.objects.create(roll_no = data['roll_no'], name = data['name'], age = data['age'])
            else:
                self.stdout.write(self.style.WARNING(f"Student with roll no: {roll_no} already exist!"))
        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))