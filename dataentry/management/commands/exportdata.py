import csv
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

from dataentry.utils import generate_csv_file

# propsed command = python manage.py exportdata model_name
class Command(BaseCommand):
    help = "Export data from the database to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help="Modle name")


    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        # search through all the installed apps for the model
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop executing once the model is found
            except LookupError:
                pass # model not found in this app, continue searching in next app

        if not model:
            self.stderr.write(f"Model {model_name} not found in any app!")
            return

        # fetch the data from the database
        data = model.objects.all()

        # generate csv file path
        file_path = generate_csv_file(model_name)

        # open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # write the CSV header
            # we want to print the field names of the model that are trying to exprot
            writer.writerow([field.name for field in model._meta.fields]) # model._meta.fields give all fields name of the model

            # write data rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
                # getattr(dt, field.name) here using getattr take all data from dt and assign it by field name that's why we use field.name if I only do 'dt for field in model._meta.fields' then it print only the value like for student the value is student name we set it using __str__() if model

        self.stdout.write(self.style.SUCCESS("Data exported successfully!"))