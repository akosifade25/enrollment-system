from django import forms
from .models import StudentAccount, Address, FamilyInformation, EducationalBackground, Subject

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# =====================================================
# REGISTER FORM
# =====================================================
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class StudentAccountForm(forms.ModelForm):
#     class Meta:
#         model = StudentAccount
#         fields = ['Student_id', 'Name', 'Email', 'Gender', 'Age']

# =====================================================
# STUDENT ACCOUNT FORM
# =====================================================
class StudentAccountForm(forms.ModelForm):
    class Meta:
        model = StudentAccount
        fields = ['Student_id', 'Name', 'Email', 'Gender', 'Age']

    def clean_student_id(self):
        student_id = self.cleaned_data.get('Student_id')
        if not student_id.isdigit():
            raise forms.ValidationError("Student ID must contain only numbers.")
        if len(student_id) < 4:
            raise forms.ValidationError("Student ID must be at least 4 digits long.")
        return student_id

    def clean_name(self):
        name = self.cleaned_data.get('Name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('Email')
        if "@" not in email or "." not in email:
            raise forms.ValidationError("Please enter a valid email address.")
        return email

    def clean_gender(self):
        gender = self.cleaned_data.get('Gender').capitalize()
        if gender not in ['Male', 'Female']:
            raise forms.ValidationError("Gender must be 'Male' or 'Female'.")
        return gender

    def clean_age(self):
        age = self.cleaned_data.get('Age')
        if age <= 0:
            raise forms.ValidationError("Age must be a positive number.")
        if age < 3 or age > 100:
            raise forms.ValidationError("Age must be between 3 and 100.")
        return age

# =====================================================
# ADDRESS FORM
# =====================================================
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['City', 'Province', 'Barangay', 'Street', 'Zip_code']

    def clean_city(self):
        city = self.cleaned_data.get('City')
        if len(city) < 3:
            raise forms.ValidationError("City name must be at least 3 characters long.")
        return city

    def clean_province(self):
        province = self.cleaned_data.get('Province')
        if not province.replace(" ", "").isalpha():
            raise forms.ValidationError("Province name must contain only letters.")
        return province

    def clean_barangay(self):
        barangay = self.cleaned_data.get('Barangay')
        if len(barangay) < 3:
            raise forms.ValidationError("Barangay name must be at least 3 characters long.")
        return barangay
    
    def clean_street(self):
        street = self.cleaned_data.get('Street')
        if len(street) < 3:
            raise forms.ValidationError("Street name must be at least 3 characters long.")
        return street

    def clean_zip_code(self):
        zip_code = self.cleaned_data.get('Zip_code')
        if not zip_code.isdigit():
            raise forms.ValidationError("Zip code must contain only numbers.")
        if len(zip_code) != 4:
            raise forms.ValidationError("Zip code must be exactly 4 digits.")
        return zip_code
    
# =====================================================
# FAMILY INFORMATION FORM
# =====================================================
class FamilyInformationForm(forms.ModelForm):
    class Meta:
        model = FamilyInformation
        fields = ['Mothers_name', 'Mothers_contact', 'Fathers_name', 'Fathers_contact', 'Guardians_name']

    def clean_mothers_name(self):
        name = self.cleaned_data.get('Mothers_name')
        if len(name) < 3:
            raise forms.ValidationError("Mother’s name must be at least 3 characters long.")
        return name

    def clean_fathers_name(self):
        name = self.cleaned_data.get('Fathers_name')
        if len(name) < 3:
            raise forms.ValidationError("Father’s name must be at least 3 characters long.")
        return name

    def clean_guardians_name(self):
        name = self.cleaned_data.get('Guardians_name')
        if len(name) < 3:
            raise forms.ValidationError("Guardian’s name must be at least 3 characters long.")
        return name

    def clean_mothers_contact(self):
        contact = self.cleaned_data.get('Mothers_contact')
        if not contact.isdigit() or len(contact) != 11:
            raise forms.ValidationError("Mother’s contact must be an 11-digit number.")
        return contact

    def clean_fathers_contact(self):
        contact = self.cleaned_data.get('Fathers_contact')
        if not contact.isdigit() or len(contact) != 11:
            raise forms.ValidationError("Father’s contact must be an 11-digit number.")
        return contact

# =====================================================
# EDUCATIONAL BACKGROUND FORM
# =====================================================
class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationalBackground
        fields = ['Elementary_school', 'Highschool', 'Senior_high', 'Tertiary', 'Year_attended']

    def clean_elementary_school(self):
        name = self.cleaned_data.get('Elementary_school')
        if len(name) < 3:
            raise forms.ValidationError("Elementary school name must be at least 3 characters long.")
        return name

    def clean_highschool(self):
        name = self.cleaned_data.get('Highschool')
        if len(name) < 3:
            raise forms.ValidationError("High school name must be at least 3 characters long.")
        return name

    def clean_tertiary(self):
        name = self.cleaned_data.get('Tertiary')
        if len(name) < 3:
            raise forms.ValidationError("Tertiary school name must be at least 3 characters long.")
        return name

    def clean_year_attended(self):
        year = self.cleaned_data.get('Year_attended')
        if not year.replace("-", "").isdigit():
            raise forms.ValidationError("Year attended must be numeric or a valid range (e.g. 2019-2023).")
        return year
    
# =====================================================
# SUBJECT FORM
# =====================================================
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['Subject_name', 'Subject_code', 'Schedule', 'Professor', 'Room_number']

    def clean_subject_name(self):
        name = self.cleaned_data.get('Subject_name')
        if len(name) < 3:
            raise forms.ValidationError("Subject name must be at least 3 characters long.")
        return name

    def clean_subject_code(self):
        code = self.cleaned_data.get('Subject_code')
        if not code.isalnum():
            raise forms.ValidationError("Subject code must contain only letters and numbers.")
        return code.upper()

    def clean_room_number(self):
        room = self.cleaned_data.get('Room_number')
        if not room.isdigit():
            raise forms.ValidationError("Room number must be numeric.")
        return room

    def clean_schedule(self):
        schedule = self.cleaned_data.get('Schedule')
        if len(schedule) < 5:
            raise forms.ValidationError("Schedule must be descriptive (e.g. MWF 9:00-10:00).")
        return schedule

    def clean_professor(self):
        name = self.cleaned_data.get('Professor')
        if len(name) < 3:
            raise forms.ValidationError("Professor name must be at least 3 characters long.")
        return name