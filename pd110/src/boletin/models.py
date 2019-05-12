from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrado(models.Model):
   nombre = models.CharField(max_length=100, blank=True, null=True)
   email = models.EmailField(max_length=254, default='ejemplo@correo.com')
   timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, default='ddmmyy')
 
    #def _str_(self)
        #return self.email