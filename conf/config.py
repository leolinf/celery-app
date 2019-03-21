# coding:utf-8
import os

HOME = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.dirname(HOME)

SERVER_NAME = 'stats'

# 日志配置
LOG_WHEN = None
LOG_FILE = {
    'root': {
        'filename': {
            'DEBUG': os.path.join(HOME, 'log/agency_statistics.log'),
            'ERROR': os.path.join(HOME, 'log/agency_statistics.error.log'),
        },
    }
}
LOG_LEVEL = 'INFO'

# 数据库配置
DATABASE = {
}
