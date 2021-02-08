from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    description = models.TextField(null=True)
    sort_order = models.IntegerField(default=1)
    url = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=True)

    SIZE_CHOICES = [
        ('img-small', 'Small'),
        ('img-large', 'Large'),
    ]

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        default='img-large',
    )

    def __str__(self):
        return self.title
