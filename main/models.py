from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Worker(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    position = models.CharField(max_length=70)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='workers')


    def __str__(self):
        return self.firstname

class Attendance(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name='attendances')
    date = models.DateField()


    def __str__(self):
        return f"{self.team} jamoasining {str(self.date)} sanadagi davomati"

class Mark(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='marks')
    worked = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='marks')
    is_attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ['attendance', 'worked']

# Create your models here.
