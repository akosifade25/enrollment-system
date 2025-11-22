from django.db import models

# Create your models here.

class StudentAccount(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    Student_id = models.CharField(max_length=100)
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.CharField(max_length=100)
    Gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    Age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.Student_id} - {self.Name}"

class Address(models.Model):
    City = models.CharField(max_length=100)
    Province = models.CharField(max_length=100)
    Barangay = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    Zip_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.City, self.Province, self.Barangay, self.Street, self.Zip_code}"
    
class FamilyInformation(models.Model):
    Mothers_name = models.CharField(max_length=100)
    Mothers_contact = models.CharField(max_length=100)
    Fathers_name = models.CharField(max_length=100)
    Fathers_contact = models.CharField(max_length=100)
    Guardians_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Mothers_name, self.Mothers_contact, self.Fathers_name, self.Fathers_contact, self.Guardians_name}"
    
class EducationalBackground(models.Model):
    Elementary_school = models.CharField(max_length=100)
    Highschool = models.CharField(max_length=100)
    Senior_high = models.CharField(max_length=100)
    Tertiary = models.CharField(max_length=100)
    Year_attended = models.IntegerField()

    def __str__(self):
        return f"{self.Elementary_school, self.Highschool, self.Senior_high, self.Tertiary, self.Year_attended}"
    
class Subject(models.Model):
    Subject_name = models.CharField(max_length=100)
    Subject_code = models.CharField(max_length=100)
    Schedule = models.CharField(max_length=100)
    Professor = models.CharField(max_length=100)
    Room_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Subject_name, self.Subject_code, self.Schedule, self.Professor, self.Room_number}"

