from django.urls import path
from .views import LessonNavList, LessonChat, GetProfile

urlpatterns = [
    path('lessons/', LessonNavList.as_view()),
    path('profile/', GetProfile.as_view()),
    path('lessons/<slug:slug>/', LessonChat.as_view()),
]
