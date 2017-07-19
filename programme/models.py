from django.db import models

import calendar

# Create your models here.

class ProgramCategory(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Program(models.Model):
    category = models.ForeignKey(ProgramCategory, related_name="program", on_delete=models.SET_NULL,blank=True, null=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Training(models.Model):
    program = models.ForeignKey(Program, related_name="training", on_delete=models.SET_NULL,blank=True, null=True)
    trainer = models.CharField(max_length=100, help_text='Trainers Name')
    rate = models.IntegerField(help_text='Training $$$')
    venue = models.CharField(max_length=100, help_text='Location of the Training(State)')
    hotel = models.CharField(max_length=100, help_text='Hotel of the Training')
    pdf = models.FileField(upload_to='uploads/', blank=True, null=True);

    def __str__(self):
        return self.trainer + " @ " + self.venue

class TrainingDate(models.Model):
    training = models.ForeignKey(Training, related_name='training_date', on_delete=models.SET_NULL,blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    # def __str__(self):
    #     return self.training.program.name +" @ " + self.training.venue + " date_id : " + str(self.id)

    def get_start_date_month_name(self):
        return calendar.month_name[self.start_date.month][:3] # First three letter of month

    def get_from_to_day(self):
        return str(self.start_date.day) + "-" + str(self.end_date.day)

    def __str__(self):
        return str(self.start_date) + " - " + str(self.end_date)

