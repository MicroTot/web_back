from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=40)
    experience  = models.CharField(max_length=40)
    expected_salary = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "User Job Descriptions"

    def __str__(self):
        return f"{self.user} is a {self.job_title} and expects a salary of {self.expected_salary}"


class Jobs(models.Model):
    job_name  = models.CharField(max_length=40)
    job_aveage_experience = models.CharField(max_length=40, verbose_name="average job experience")
    job_average_salary = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Jobs"

    def __str__(self):
        return f"{self.job_name}"
