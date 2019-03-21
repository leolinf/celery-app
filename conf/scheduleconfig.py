# coding=utf-8
from celery.schedules import crontab

CELERY_TIMEZONE = 'Asia/Shanghai'

 # 请统一配置contab，否则monitor无法识别
 # 目前允许配置两种形式：
 # 1.每天固定时间点: crontab(hour=12, minute=0)
 # 2.间隔时间点: crontab(hour='*/2', minute=0) 0点开始，每2h执行一次
CELERYBEAT_SCHEDULE = {
    'test': {
        'task': 'test.add',  # 指定对应的定时任务
        'schedule': crontab(hour='*/1', minute=45),  # 指定对应的时间
        'args': (1, 1),  # 参数
        'options': {'exchange': 'ex.test', 'routing_key': 'test'},  # 指定对应的 exchange 和 routing_key 找到相应的队列
    },
}
