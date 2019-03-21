# coding: utf-8
import logging
import traceback

from celery import Task
from celery.utils.log import get_task_logger

from conf import config

clogger = get_task_logger(__name__)
log = logging.getLogger()


class BaseTask(Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """任务失败回调函数

            1.异常抛到celery层
            2.task retry已到达最大值
        """
        log.warn('task fail! id=%s, name=%s, args=%s, kwargs=%s, einfo=%s',
                 task_id, self.name, args, kwargs, einfo)
        return super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)
