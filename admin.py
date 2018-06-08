from django.contrib import admin

# Register your models here.
from main.models import Subtopic, Topic, Data, Test, Usertest, Question, Answer, Course, User

admin.site.register(Course)
admin.site.register(Test)
admin.site.register(Usertest)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Data)
admin.site.register(User)