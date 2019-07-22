from django.urls import path
from classroom import views

urlpatterns = [
    path('', views.index, name = "get_recommended_courses"),
    path('courses/', views.courses, name = "get_all_courses"),
    path('courses/<int:id>', views.singleCourse, name = "get_course"),
    path('courses/<int:course_id>/content/<int:content_id>', views.content, name = 'get_content')
]