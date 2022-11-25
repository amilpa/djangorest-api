from django.db import models

# Create your models here.


class WorkerManagement(models.Model):
    customername = models.CharField(max_length = 200 ,null = True)
    customeraddress = models.TextField(max_length = 500 , null = True)
    updated = models.DateTimeField(auto_now=True , null=True)
    created = models.DateTimeField(auto_now_add=True , null = True)

    def __str__(self):
        return self.agentname[0:50]

    class Meta:
        ordering = ['-updated']

