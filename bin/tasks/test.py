# coding: utf-8
import time

from celery import group
from celery.utils.log import get_task_logger

from bin.tasks import app
from bin.tasks.base import BaseTask
from conf import config

clogger = get_task_logger(__name__)


@app.task(base=BaseTask, name='test.calu')
def calu(x, y):
    multi(x, y)


@app.task(base=BaseTask, bind=True, name='test.add')
def add(self, x, y):
    #clogger.info(self.request.__dict__)
    #raise KeyError
    #time.sleep(3)
    return x + y


def multi(x, y):
    x = x * y
    return process.delay(x, y)


@app.task(base=BaseTask, bind=True, name='test.adds')
def adds(self):
    group(add.s(i, i) for i in xrange(10)).delay()


@app.task(base=BaseTask, name='test.process')
def process(x, y):
    return x*10 + y*10
