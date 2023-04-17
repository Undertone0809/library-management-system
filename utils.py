# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 17:29
# @Author  : Zeeland
# @File    : utils.py
# @Software: PyCharm

import os
import time
import hashlib
import logging
import platform
import datetime
from functools import wraps
from typing import Optional, Union, List

cur_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
logger = logging.getLogger(__name__)


def generate_id() -> str:
    """
    generate a model id
    :return:
    """
    return str(time.time())


def _get_project_root_path() -> str:
    project_path = os.getcwd()
    max_depth = 10  # 最大循环次数
    count = 0
    while not os.path.exists(os.path.join(project_path, 'README.md')):
        project_path = os.path.split(project_path)[0]
        count += 1
        if count > max_depth:  # 超出最大循环次数
            raise Exception('Could not find project root directory.')
    return project_path


def _check_log_path():
    log_path = os.path.join(_get_project_root_path(), 'log')
    if not os.path.exists(log_path):
        os.makedirs(log_path)


def _get_log_name() -> str:
    return f"{_get_project_root_path()}/log/log_{cur_time}.log"


def get_cache_path():
    return f"{_get_project_root_path()}/data"


def get_md5(dic: dict):
    return hashlib.md5(str(dic).encode("utf-8")).hexdigest()


def is_equals(dic1: dict, dic2: dict):
    return hashlib.md5(str(dic1).encode("utf-8")).hexdigest() == hashlib.md5(str(dic2).encode("utf-8")).hexdigest()


def enable_log():
    if platform.system() == 'Windows':
        _check_log_path()
        # todo 检查日志输出为空的问题
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(levelname)s] %(asctime)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                logging.FileHandler(f"{_get_log_name()}", mode='w', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )


def enable_log_no_file():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] %(asctime)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )


def hint(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        logger.debug(f'function {fn.__name__} is running now')
        return ret

    return wrapper
