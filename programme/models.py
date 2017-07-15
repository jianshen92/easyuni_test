from django.db import models

# Create your models here.

class ProgramCategory(models.Model):
    name = models.CharField(max_length=500)

class Program(models.Model):
    category = models.ForeignKey(ProgramCategory, on_delete=models.SET_NULL,blank=True, null=True)
    name = models.CharField(max_length=500)

class Training(models.Model):
    program = models.ForeignKey(Program, on_delete=models.SET_NULL,blank=True, null=True)
    trainer = models.CharField(max_length=100, help_text='Trainers Name')
    rate = models.IntegerField(help_text='Training $$$')
    venue = models.CharField(max_length=100, help_text='Location of the Training(State)')
    hotel = models.CharField(max_length=100, help_text='Hotel of the Training')

class TrainingDate(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    pdf = models.FileField(upload_to='uploads/');
