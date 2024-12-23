from django.contrib import admin

from .models import Student, Teacher


class StudentTeachersInline(admin.TabularInline):
    # model = StudentTeachers
    model = Student.teachers.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    list_filter = ['group']
    inlines = [StudentTeachersInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['subject']
    inlines = [StudentTeachersInline]
