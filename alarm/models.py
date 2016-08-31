from __future__ import unicode_literals

from django.db import models

class Alarm(models.Model):
	alarm = models.DateTimeField()
	ip_address = models.GenericIPAddressField()

	def __unicode__(self):
		return u'Alarm : %s \nIP : %s' % (self.alarm, self.ip_address)
