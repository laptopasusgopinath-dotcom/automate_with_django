from awd_main.celery import app
from django.core.management import call_command
import time
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import send_email_notification, generate_csv_file

@app.task
def celery_test_task():
    time.sleep(5) # simulation of any task that's going to take 10 seconds
    # send an email
    # EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail_subject = 'Test subject'
    message = 'This is a test email'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return "Email sent successfully."

@app.task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata', file_path, model_name) # call_command is user for to trigger command and for trigger importdata script we need two argument 'file_path' and 'model_name'
    except Exception as e:
        raise e   
    # notify the user by email 
    mail_subject = 'Import Data Completed'
    message = 'Your data import has been successful'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return 'Data imported successfully.'


@app.task
def export_data_task(model_name):
    try:
        call_command('exportdata', model_name)
    except Exception as e:
        raise e
    
    file_path = generate_csv_file(model_name)
    
    # Send email with the attachment
    mail_subject = 'Export Data Successful'
    message = 'Your data export has been successful. Please find the attachment.'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email, attachment=file_path)
    return 'Export Data task executed successfully.'





