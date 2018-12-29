from django.db.models import Model
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import FriendValidator

FriendlyNameValidator=FriendValidator


class UrlEntry(models.Model):
        #auto_increment_id=models.AutoField(primary_key=True,default=1,unique=True)
        FriendlyName= models.CharField(max_length=10,
        help_text=_('Type in a friendly name you would like to use and we will check if it is available'),
        validators=[FriendlyNameValidator],
        error_messages={
            'unique': _("This friendly name is unavailabe.")
        }
        )
        ShortUrl= models.CharField(max_length=128)
        OriginDomain = models.URLField()
        Views = models.IntegerField(default=0)
        OriginIp = models.CharField(max_length=128)
        FriendlyKey= models.IntegerField(default=0)
        
        def __unicode__(self):
            return self.title