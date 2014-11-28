from django.db import models

# Create your models here.
class Project(models.Model):
    projectname = models.CharField(max_length=200, unique=True)
    summary = models.TextField(max_length=500, unique=True)
    src_url = models.URLField()
    doc_url = models.URLField()
    apk = models.FileField(upload_to='apk')
    logo = models.ImageField(upload_to='project_logo', blank=True)

    def __unicode__(self):
        return self.projectname

