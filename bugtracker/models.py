from django.db import models

class Bug(models.Model):
    bug_id = models.AutoField(primary_key=True)
    bug_type = models.CharField(max_length=100)
    bug_description = models.TextField()
    company_affected = models.CharField(max_length=50)
    domains_affected = models.TextField()
    date_of_capture = models.DateTimeField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.company_affected

