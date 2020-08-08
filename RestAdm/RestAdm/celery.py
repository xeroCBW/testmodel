from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
# set the default Django settings module for the 'celery' program.
from RestAdvanceAdm import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RestAdm.settings')

app = Celery('RestAdm')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
app.autodiscover_tasks(settings.INSTALLED_APPS)


# 设置使用远程的rabbit
app = Celery('website', backend='amqp', broker='amqp://ccc:123456qwer@120.24.167.214')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))