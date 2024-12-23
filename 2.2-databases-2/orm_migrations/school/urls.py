from django.contrib import admin
from django.urls import path

from school.views import students_list, teachers_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', students_list, name='students'),
    path('teacher/', teachers_list, name='teachers')
]
