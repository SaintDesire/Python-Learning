from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    addDate = models.DateTimeField(null=True)
    dueDate = models.DateField(null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/todo/{self.id}'

    class Meta:
        verbose_name = "Todo"
