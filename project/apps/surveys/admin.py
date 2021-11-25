from django.contrib import admin

from apps.surveys.models import Survey, Answer, Question


admin.site.register(Survey)
admin.site.register(Answer)
admin.site.register(Question)