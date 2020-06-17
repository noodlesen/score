from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Chapter(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField()


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    block = models.ForeignKey(
        Chapter,
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField()


class Bit(models.Model):
    name = models.CharField(max_length=255)
    MEDIA_CHOICES = [
        ('TEXT', 'Text'),
        ('IMAGE', 'Image'),
        ('VIDEO', 'Video')
    ]
    media = models.CharField(
        max_length=5,
        choices=MEDIA_CHOICES,
        default=None,
        null=True
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField()
