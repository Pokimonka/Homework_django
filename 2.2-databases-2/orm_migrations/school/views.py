from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    obj = Student.objects.order_by(ordering)
    context = {
        'object_list': obj
    }

    return render(request, template, context)



def teachers_list(request):
    template = 'school/teachers_list.html'
    ordering = 'subject'
    obj = Teacher.objects.order_by(ordering)
    context = {
        'object_list': obj
    }

    return render(request, template, context)
