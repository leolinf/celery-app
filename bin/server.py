# coding: utf-8
import logging
import os
import sys

import dbenc

HOME = os.path.dirname(os.path.abspath(__file__))
sys.path.append(HOME)
sys.path.append(os.path.dirname(HOME))

log = logging.getLogger()


def install_db():
    pass


def load_tasks():
    """celery 起服务时加载task模块"""

    log.info('<<< LOAD TASKS>>>')
    from bin.tasks import test


install_db()
load_tasks()
