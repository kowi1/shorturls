from django.db.models import Model
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import FriendValidator

friendlyname_validator=FriendValidator

class uniqueUrl(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __unicode__(self):
        return self.name

class UrlEntry(models.Model):
       # origin_url= models.ForeignKey(uniqueUrl,on_delete=models.PROTECT)
        friendly_name= models.CharField(max_length=128,
        help_text=_('Type in a friendly name you would like to use and we will check if it is available'),
        validators=[friendlyname_validator],
        error_messages={
            'unique': _("This friendly name is unavailabe.")
        }
        )
        short_url= models.URLField()
        origin_domain = models.URLField()
        views = models.IntegerField(default=0)
        origin_ip = models.CharField(max_length=128)
        
        def __unicode__(self):
            return self.title