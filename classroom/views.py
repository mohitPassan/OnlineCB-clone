from django.shortcuts import render
from classroom import models
# Create your views here.

def index(request):
    courses = models.Course.objects.all()
    Context = {
        "recommended_courses": courses
    }
    return render(request, 'classroom/index.html', Context)

def courses(request):
    courses = models.Course.objects.all()

    Context = {
        "courses": courses
    }

    return render(request, 'classroom/courses.html', Context)

def singleCourse(request, id):
    course = models.Course.objects.get(id = id)

    Context = {
        "course" : course
    }

    return render(request, 'classroom/singleCourse.html', Context)
