from django.urls import path
from classroom import views

urlpatterns = [
    path('', views.index),
    path('courses/', views.courses),
    path('courses/<int:id>', views.singleCourse)
]