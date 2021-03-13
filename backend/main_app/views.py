from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Lesson, Chat, Messages
from .serializers import LessonSerializer, ChatSerializer, ProfileSerializer


class LessonNavList(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class GetProfile(APIView):
    def get(self, request):
        profile = get_object_or_404(Token, key=self.request.META.get('HTTP_AUTHORIZATION')).user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class LessonChat(APIView):
    def get_user(self, request):
        try:
            user = Token.objects.get(key=request.META.get('HTTP_AUTHORIZATION')).user
            return user
        except Token.DoesNotExist:
            raise PermissionDenied()

    def get_lesson(self, user, slug):
        lesson = get_object_or_404(Lesson, slug=slug)
        if lesson.managers.filter(user=user).exists() or lesson.students.filter(user=user).exists():
            return lesson
        else:
            raise PermissionDenied()

    def get(self, request, slug):
        user = self.get_user(request)
        lesson = self.get_lesson(user, slug)

        if user.profile.status == "student":
            chat, created = Chat.objects.get_or_create(user=user.profile, lesson=lesson)
            chat = [chat, ]
            serializer = ChatSerializer(chat, many=True)
        else:
            chats = Chat.objects.filter(lesson=lesson)
            serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, slug):
        user = self.get_user(request)
        lesson = self.get_lesson(user, slug)
        if user.profile.status == "student":
            chat, created = Chat.objects.get_or_create(user=user.profile, lesson=lesson)
        else:
            chat = Chat.objects.filter(lesson=lesson)[0]
        Messages.objects.create(chat=chat, who_wrote=user.profile.status, message=request.data['message'])
        return Response(status=204)
