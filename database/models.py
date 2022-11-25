from django.db import models

# Create your models here.


class WorkerManagement(models.Model):
    customeremail = models.EmailField(primary_key = True , default = "amilpa2020@gmail.com")
    customername = models.CharField(max_length = 200  )
    customeraddress = models.TextField(max_length = 500)
    updated = models.DateTimeField(auto_now=True )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agentname[0:50]

    class Meta:
        ordering = ['-updated']

