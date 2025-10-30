from django.db import models

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - {"completed" if self.completed else "not completed"}'
