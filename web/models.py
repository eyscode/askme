from django.db import models

# Create your models here.


class Pregunta(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    aproved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #creator = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = "-created_at",