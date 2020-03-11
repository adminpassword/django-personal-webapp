from django.contrib import admin

from .models import Question


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    readonly_fields = ('id',)



admin.site.register(Question, QuestionAdmin)
