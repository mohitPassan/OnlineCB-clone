from django.urls import path
from classroom import views

urlpatterns = [
    path('', views.Index.as_view(), name = "get_recommended_courses"),
    path('courses/', views.Courses.as_view(), name = "get_all_courses"),
    path('courses/<int:pk>', views.SingleCourse.as_view(), name = "get_course"),
    path('courses/<int:course_id>/content/<int:pk>', views.Content.as_view(), name = 'get_content')
]