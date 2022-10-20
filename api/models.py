from cgitb import enable
from email.policy import default
from django.db import models
from django.utils.text import slugify


# Create your models here.

class QuestionSet(models.Model):
    name = models.CharField(max_length=240)
    slug = models.CharField(max_length=120, blank=True, null=True)
    enable_neg_marking = models.BooleanField(default=False)
    negative_marking_percentage=models.IntegerField(blank=True,null=True)
    ideal_time_to_complete= models.IntegerField()

    def __str__(self):
        return self.slug
    
    def save(self , *args, **kwargs):
        if self.slug:
            super(QuestionSet, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.name)
            super(QuestionSet, self).save(*args, **kwargs)

class Question(models.Model):
    CHOICES =  (
        ('MCQWithRadio', 'Radio'),
        ('MCQWithCheckBox', 'Checkbox'),
        ('Matrix', 'Matrix'),
    )
    id_questionset=models.ForeignKey(to=QuestionSet, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=240, blank=True, null=True)
    question_image= models.ImageField(blank=True,null=True)
    question_type = models.CharField(max_length=300, choices = CHOICES)
    question_order=models.IntegerField()
    question_marks=models.IntegerField()
    
    def __str__(self):
        return self.question_text

class QuestionOptions(models.Model):
    id_question=models.ForeignKey(to=Question, on_delete=models.CASCADE)
    option_text=models.CharField(max_length=240, blank=True, null=True)
    option_image=models.ImageField(blank=True, null=True)
    option_order=models.IntegerField(default=1)
    correct_answer=models.BooleanField(default=False)
    marks=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.option_text
        

class GroupQuestion(Question):
    pass

class groupInlineQuestions(models.Model):
    Id_group_question=models.ForeignKey(to=GroupQuestion, related_name='groupquestion', on_delete=models.CASCADE)
    Id_question=models.ForeignKey(to=Question, related_name='question', on_delete=models.CASCADE)
    question_order=models.IntegerField()
    question_marks=models.IntegerField()
