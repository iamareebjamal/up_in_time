from django.conf.urls import url
from django.contrib import admin

import alarm.views as av

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alarm/$', av.alarm),
    url(r'^success/$', av.create_alarm)
]