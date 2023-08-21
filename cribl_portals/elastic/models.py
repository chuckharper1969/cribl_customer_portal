from django.db import models

class ElasticDestination(models.Model):
    STATUSES = [
        (0, "Onboarding"),
        (1, "OK"),
        (2, "Disabled"),
        (3, "Failure"),
    ]
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=128)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    url = models.CharField(max_length=256)
    message = models.CharField(max_length=128, default="Waiting to be onboarded")
    status = models.IntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return(self.title)

class ElasticDestinationUpdate(models.Model):
    STATUSES = [
        (0, "Onboarding"),
        (1, "OK"),
        (2, "Disabled"),
        (3, "Failure"),
    ]
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=128)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    url = models.CharField(max_length=256)
    message = models.CharField(max_length=128, default="Waiting to be onboarded")
    status = models.IntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return(self.title)
    