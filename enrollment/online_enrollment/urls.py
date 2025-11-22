from django.contrib import admin
from django.urls import path
from online_enrollment import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register_user'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('students/', views.student_account_view, name='student_account'),
    path('address/', views.address_view, name='address'),
    path('family/', views.family_view, name='family'),
    path('education/', views.education_view, name='education'),
    path('subjects/', views.subject_view, name='subject'),

    path('add_student/', views.add_student_view, name='add_student'),
    path('edit-student/<int:student_id>/', views.edit_student_view, name='edit_student'),

    path('success/', views.success, name='success'),
]
