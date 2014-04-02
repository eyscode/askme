from django.contrib.auth.models import User
from django.db import models
from web.utils import SumWithDefault


class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    aproved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = "-created_at",

    def last_5_answers(self):
        return self.answers.annotate(points=SumWithDefault('votes__plusone', default=0)).all().order_by('-points')[:5]


class Answer(models.Model):
    question = models.ForeignKey('Question', related_name='answers')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.content[:10]

    class Meta:
        ordering = '-created_at',


class Vote(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey('Answer', related_name='votes')
    plusone = models.IntegerField(default=True)

    class Meta:
        unique_together = 'user', 'answer'