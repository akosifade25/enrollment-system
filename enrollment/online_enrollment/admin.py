from django.contrib import admin
from .models import StudentAccount, Address, FamilyInformation, EducationalBackground, Subject

# Register your models here.
admin.site.register(StudentAccount)
admin.site.register(Address)
admin.site.register(FamilyInformation)
admin.site.register(EducationalBackground)
admin.site.register(Subject)