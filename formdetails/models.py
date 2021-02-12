from django.db import models
from django.utils import timezone
# Create your models here.
class studentdetails(models.Model):
    student_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    school=models.CharField(max_length=60)
    board=models.CharField(max_length=60)
    standard=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    category=models.CharField(max_length=200,default="")
    number=models.CharField(max_length=20)
    registerdate = models.DateTimeField(default=timezone.now())