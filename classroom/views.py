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

def content(request, course_id, content_id):
    course = models.Course.objects.get(id = course_id)
    content = course.contents.get(id = content_id)

    Context = {
        "content": content
    }

    template_name = ''
    if content.content_type == 'pdf':
        template_name = 'content_pdf.html'
    elif content.content_type == 'youtube':
        template_name = 'content_yt.html'
    elif content.content_type == 'image':
        template_name = 'content_img.html'

    return render(request, 'classroom/{}'.format(template_name), Context)