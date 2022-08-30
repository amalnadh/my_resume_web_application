from django.db import models

# Create your models here.
class Profile(models.Model):
    picture=models.ImageField(upload_to='profile',blank=True)
    career=models.CharField(max_length=100)
    summary=models.TextField()
    place=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    email=models.EmailField()



class Experience(models.Model):
    jobposition=models.CharField(max_length=250)
    company=models.CharField(max_length=250)
    description=models.TextField(blank=True)
    startdate=models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return self.jobposition


class Educations(models.Model):
    university=models.CharField(max_length=250)
    degree=models.CharField(max_length=250)
    startdate=models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return self.university


class Certification(models.Model):
    cert_name=models.CharField(max_length=255)


    def __str__(self):
        return self.cert_name


class Projects(models.Model):
    project_name=models.CharField(max_length=255)
    project_desc=models.TextField()
    project_link=models.URLField(max_length=255)

    def __str__(self):
        return self.project_name

