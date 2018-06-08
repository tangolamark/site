from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
from django.db.models.signals import post_save
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название курса')
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def make_used(self):
        return reverse('StartCourse', args=[self.pk])

    def get_absolute_url(self):
        return reverse('Topic', args=[self.pk])

class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название темы')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('TopicDataView', args=[self.pk])

class Subtopic(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название подтемы')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('DataView', args=[self.pk])


class Data(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название параграфа')
    text = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to="img/", blank='True', verbose_name='Пояснение')
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Test(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название теста')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    desc = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('QuesView', args=[self.pk])

class Usertest(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя юзера в тесте')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    score = models.FloatField(default=0)
    data_start = models.DateTimeField(auto_now_add=True, auto_now=False)
    comment = models.TextField(blank='True', verbose_name='Комментарий к тесту')

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=1234, verbose_name='Вопрос')

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=1234, verbose_name='Ответ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

class User(AbstractUser):
    study_group = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    url = models.URLField()


# class UserProfile(User):
#     group = models.CharField(max_length=200, verbose_name="Группа", default='ip413')
#
# class UserProfile(User):
#     # username = models.CharField(max_length=100, verbose_name="Логин", default="login")
#     # first_name = models.CharField(max_length=100, verbose_name="Имя", default="imya")
#     # last_name = models.CharField(max_length=100, verbose_name="Фамилия", default="familiya")
#     # email = models.CharField(max_length=100, verbose_name="Почта", default="mail@mail.ru")
#     group = models.CharField(max_length=100, verbose_name="Группа", default="ip111")
#
#     def __str__(self):
#         return self.username


# class UP(User):
#     text = models.CharField(max_length=100, verbose_name="Тест")

# class UserPrifile(models.Model):
#     user = models.OneToOneField(User)
#     avatar = models.ImageField(verbose_name='Изображение')

# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#
#     textovoe = models.CharField(max_length=200, verbose_name='Буквы')
#
#
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             UserProfile.objects.create(user=instance)
#
#     post_save.connect(create_user_profile, sender=User)