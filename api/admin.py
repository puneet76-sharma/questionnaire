from django.contrib import admin
from .models import Question,QuestionSet,QuestionOptions,GroupQuestion,groupInlineQuestions

# Register your models here.

class QuestionSetAdmin(admin.ModelAdmin):
        list_display = [
        'id', 'name', 'slug', 'enable_neg_marking', 'negative_marking_percentage',
        'ideal_time_to_complete'
        ]

class QuestionOptionsAdmin(admin.TabularInline):
    extra = 4
    model = QuestionOptions   

class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'id_questionset', 'question_text', 'question_type', 'question_order',
        'question_marks'
        ]
    inlines = [QuestionOptionsAdmin]

class groupInlineQuestionsAdmin(admin.TabularInline):
    extra = 4
    model = groupInlineQuestions 
    fk_name = 'Id_group_question'  

class GroupQuestionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'id_questionset', 'question_text', 'question_type', 'question_order',
        'question_marks'
        ]
    inlines = [groupInlineQuestionsAdmin]


admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(GroupQuestion, GroupQuestionAdmin)


