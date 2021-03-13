from rest_framework import serializers
from .models import Lesson, Chat, UserProfile, Messages


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'slug')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('full_name', 'status')


class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    access = serializers.IntegerField(default=1)
    messages = MessagesSerializer(many=True)
    user = ProfileSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Chat
        fields = ('access', 'user', 'messages', 'lesson')
