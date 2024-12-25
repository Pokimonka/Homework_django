import pytest
from django.conf import settings
from model_bakery import baker
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient
import random
from students.models import Student, Course

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    course = course_factory(_quantity = 10)
    response = client.get('/courses/1/')

    assert response.status_code == 200

    data = response.json()

    assert data['name'] == course[0].name


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity = 20)

    response = client.get('/courses/')

    assert response.status_code == 200

    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
       assert c['name'] == courses[i].name


@pytest.mark.django_db(reset_sequences=True)
def test_get_course_by_id(client, course_factory):
    course = course_factory(_quantity = 20)
    select_num = random.randint(0, 19)
    response = client.get(f'/courses/?id={select_num}')

    assert response.status_code == 200

    data = response.json()
    assert data[0]['id'] == select_num

@pytest.mark.django_db
def test_get_course_by_name(client, course_factory):
    course = course_factory(_quantity = 20)
    rand_numb = random.randint(0, 19)
    selected_course_name = course[rand_numb].name
    response = client.get(f'/courses/?name={selected_course_name}')

    assert response.status_code == 200

    data = response.json()
    assert data[0]['name'] == selected_course_name

@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    data = {
        'name': 'Math',
        'students': []
    }
    response = client.post('/courses/', data=data)

    resp = response.json()
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert Course.objects.values()[0]['name'] == resp['name']

@pytest.mark.django_db
def test_create_course_with_students(client, course_factory, student_factory):
    course = course_factory(_quantity=1)
    students = student_factory(_quantity=20)
    course[0].students.add(*students)

    response = client.get('/courses/')

    assert response.status_code == 200

    data = response.json()

    assert course[0].id == data[0]['id']
    assert course[0].name == data[0]['name']
    assert [s.id for s in students] == [s['id'] for s in data[0]['students']]


@pytest.fixture
def settings_max_students(settings):
    settings.MAX_STUDENTS_PER_COURSE = 20
    return settings


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.parametrize(
    'student, need_raise',
    (
            (settings.MAX_STUDENTS_PER_COURSE+1, True),
            (settings.MAX_STUDENTS_PER_COURSE,  False),
            (settings.MAX_STUDENTS_PER_COURSE-1 , False),
    )
)
def test_validate_max_students(client, student, need_raise, course_factory, student_factory):
    course = course_factory(_quantity=1)
    students = student_factory(_quantity=student)
    course[0].students.add(*students)
    if need_raise:
        with pytest.raises(ValidationError):
            course[0].clean()








