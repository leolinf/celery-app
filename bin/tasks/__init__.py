from celery import Celery
from conf import celeryconfig

app = Celery('stats')
app.config_from_object(celeryconfig)
