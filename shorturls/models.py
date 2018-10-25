from django.db.models import Model
from django.db import models
class uniqueUrl(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return self.name

class UrlEntry(models.Model):
       # origin_url= models.ForeignKey(uniqueUrl,on_delete=models.PROTECT)
        friendly_name= models.CharField(max_length=128)
        short_url= models.URLField()
        origin_domain = models.URLField()
        views = models.IntegerField(default=0)
        origin_ip = models.IntegerField(default=0)
        
        def __unicode__(self):
            return self.title