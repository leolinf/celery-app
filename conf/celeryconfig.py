# coding=utf-8
from kombu import Queue, Exchange
from conf.scheduleconfig import *

#  Broker settings.
BROKER_URL = 'redis://localhost:6379/6'
BROKER_POOL_LIMIT = 20

CELERY_RESULT_BACKEND = 'redis://localhost:6379/7'
CELERY_TASK_RESULT_EXPIRES = 60 * 60

CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_MESSAGE_COMPRESSION = 'gzip'

# enable client to sent a task-sent event when it occurr
CELERY_SEND_TASK_SENT_EVENT = True
CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_PREFETCH_MULTIPLIER = 10

CELERY_QUEUES = (
    Queue('test',
          exchange=Exchange('ex.test', type='direct'),
          routing_key='test'),
)

CELERY_ROUTES = ([
    ('rd.group.test.*', {
        'exchange': 'rd.qudao.ex.test',
        'routing_key': 'test'
    }),
],)
