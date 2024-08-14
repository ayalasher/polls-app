from django.db import models

# Create your models here.
class Question(models.Model):
    text_question = models.CharField(max_length=255)
    pub_date = models.DateTimeField("Date published")


class choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)