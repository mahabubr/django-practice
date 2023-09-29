from .views import StudentView
from django.urls import path

urlpatterns = [
    path("basic/", StudentView.as_view()),
    path("basic/<int:id>/", StudentView.as_view(), name="student-detail"),
]
