from django.db.models import Model
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import FriendValidator

friendlyname_validator=FriendValidator


class UrlEntry(models.Model):
        #auto_increment_id=models.AutoField(primary_key=True,default=1,unique=True)
        friendly_name= models.CharField(max_length=128,
        help_text=_('Type in a friendly name you would like to use and we will check if it is available'),
        validators=[friendlyname_validator],
        error_messages={
            'unique': _("This friendly name is unavailabe.")
        }
        )
        short_url= models.CharField(max_length=128)
        origin_domain = models.URLField()
        views = models.IntegerField(default=0)
        origin_ip = models.CharField(max_length=128)
        friendly_key= models.IntegerField(default=0)
        
        def __unicode__(self):
            return self.title