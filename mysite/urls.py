from django.conf.urls import url
from django.contrib import admin

import alarm.views as av

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alarm/$', av.alarm),
    url(r'^time', av.set_alarm_with_time),
    url(r'^duration/', av.set_alarm_with_duration),
    url(r'^templates/alarm_set$', av.msg_set),
]