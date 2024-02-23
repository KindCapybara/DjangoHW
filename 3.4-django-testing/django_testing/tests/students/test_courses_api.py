from model_bakery import baker
from rest_framework.test import APIClient
import pytest
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
def test_get_one_course(client, course_factory):
    courses = course_factory(_quantity=1)
    course_id = courses[0].id
    response = client.get(f'/api/v1/courses/{course_id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == courses[0].name


@pytest.mark.django_db
def test_get_course_list(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_get_filter_id_course(client, course_factory):
    courses = course_factory(_quantity=10)
    course_id = courses[0].id
    response = client.get('/api/v1/courses/', data={'id': course_id})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[0].id


@pytest.mark.django_db
def test_get_filter_name_course(client, course_factory):
    courses = course_factory(_quantity=10)
    course_name = courses[0].name
    response = client.get('/api/v1/courses/', data={'name': course_name})
    assert response.status_code == 200
    data = response.json()
    for i, course in enumerate(data):
        assert course['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    course = {'name': 'Test_Course'}
    response = client.post(f'/api/v1/courses/', data=course)
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    course = {'name': 'Test_Course'}
    response = client.put(f'/api/v1/courses/{courses[3].id}/', data=course)
    data = response.json()
    assert course['name'] == data['name']
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.delete(f'/api/v1/courses/{courses[3].id}/')
    assert response.status_code == 204
