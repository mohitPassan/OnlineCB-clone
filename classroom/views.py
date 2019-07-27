from django.shortcuts import render
from classroom import models
from django.views.generic import View, ListView, DetailView
# Create your views here.

class Index(View):
    def get(self, request):
        courses = models.Course.objects.all()
        Context = {
            "recommended_courses": courses
        }
        return render(request, 'classroom/index.html', Context)

# def index(request):
#     courses = models.Course.objects.all()
#     Context = {
#         "recommended_courses": courses
#     }
#     return render(request, 'classroom/index.html', Context)

class Courses(ListView):
    model = models.Course
    template_name = 'classroom/courses.html'
    context_object_name = 'courses'

# def courses(request):
#     query = request.GET.get('query', '')
#     courses = models.Course.objects.filter(name__icontains = query)

#     Context = {
#         "courses": courses
#     }

# return render(request, 'classroom/courses.html', Context)

class SingleCourse(DetailView):
    model = models.Course
    template_name = 'classroom/singleCourse.html'
    context_object_name = 'course'

# def singleCourse(request, id):
#     course = models.Course.objects.get(id = id)

#     Context = {
#         "course" : course
#     }

#     return render(request, 'classroom/singleCourse.html', Context)

class Content(DetailView):
    def get_queryset(self):
        return models.Course.objects.get(id = self.kwargs['course_id']).contents

    def get_template_names(self):
        content = self.get_object()
        template_name = ''
        if content.content_type == 'pdf':
            template_name = 'classroom/content_pdf.html'
        elif content.content_type == 'youtube':
            template_name = 'classroom/content_yt.html'
        elif content.content_type == 'image':
            template_name = 'classroom/content_img.html'
        return template_name


# def content(request, course_id, content_id):
#     course = models.Course.objects.get(id = course_id)
#     content = course.contents.get(id = content_id)

#     Context = {
#         "content": content
#     }

#     template_name = ''
#     if content.content_type == 'pdf':
#         template_name = 'content_pdf.html'
#     elif content.content_type == 'youtube':
#         template_name = 'content_yt.html'
#     elif content.content_type == 'image':
#         template_name = 'content_img.html'

#     return render(request, 'classroom/{}'.format(template_name), Context)