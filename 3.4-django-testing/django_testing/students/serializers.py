from django_filters.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from students.models import Course, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "name", "birth_date")

class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, attrs):
        course = Course.objects.filter(name=attrs['name']).values()
        print(attrs)
        if course:
            count_stud = course.get('student').count()
            if count_stud > settings.MAX_STUDENTS_PER_COURSE:
                raise ValidationError('Слишком много студентов, мы не вывозим')
        return attrs