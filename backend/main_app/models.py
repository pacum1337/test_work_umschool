from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
PERSONS = (
    ('student', 'Студент'),
    ('manager', 'Менеджер')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField("Полное имя", max_length=150)
    status = models.CharField('Статус пользователя', max_length=50, choices=PERSONS, null=True)

    def __str__(self):
        return f'{self.full_name} - {self.status}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Lesson(models.Model):
    name = models.CharField("Название предмета", max_length=50)
    slug = models.SlugField('URL', max_length=50, unique=True)
    managers = models.ManyToManyField(UserProfile, verbose_name='Менеджеры, что имеют доступ к предмету',
                                      related_name='managers')
    students = models.ManyToManyField(UserProfile, verbose_name='Студенты, что имеют доступ к предмету',
                                      related_name='students')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Chat(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='Студент', on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, verbose_name='Предмет', on_delete=models.CASCADE)

    def __str__(self):
        return f'Чат по предмету {self.lesson} со студентом {self.user.full_name}'

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Messages(models.Model):
    chat = models.ForeignKey(Chat, verbose_name='Чат', on_delete=models.CASCADE, related_name='messages')
    who_wrote = models.CharField('Кто написал?', max_length=50, choices=PERSONS)
    message = models.TextField('Сообщение', max_length=500)

    def __str__(self):
        return f'{self.chat} - {self.who_wrote}'

    class Meta:
        verbose_name = 'Сообшение'
        verbose_name_plural = 'Сообщения'
