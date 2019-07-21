from django.shortcuts import render
from classroom import models
# Create your views here.

def index(request):
    courses = models.Course.objects.all()
    Context = {
        "recommended_courses": courses
    }
    return render(request, 'classroom/index.html', Context)

def course(request, id):
    course = models.Course.objects.get(id = id)

    Context = {
        "course": course
    }

    return render(request, 'classroom/course.html', Context)
