from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
    # question_text is the field's name in machine-friendly format
    question_text = models.CharField(max_length=200)
    # introduced human-readable name 'date published' as first argument of Field instance
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now

    was_published_recently.short_description = 'Published recently?#'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    # find out more on def __str__ method outside Django context
