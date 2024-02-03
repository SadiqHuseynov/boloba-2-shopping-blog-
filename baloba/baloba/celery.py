from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baloba.settings")
app = Celery("baloba")
app.conf.enable_utc=False
app.config_from_object("django.conf.settings", namespace="CELERY")
app.autodiscover_tasks()
