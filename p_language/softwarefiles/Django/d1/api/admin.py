from django.contrib import admin
from api.models import Question,Choice
admin.site.register(Question)
# Register your models here.
admin.site.register(Choice)
