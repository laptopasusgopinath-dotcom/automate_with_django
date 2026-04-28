from django.db import models

# Create your models here.

class Upload(models.Model):
    file = models.FileField(upload_to='uploads/') # It store the file path and file are store in uploads folder
    model_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name