# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 17:29
# @Author  : Zeeland
# @File    : utils.py
# @Software: PyCharm

import os
import time
import hashlib
import logging
import datetime
from typing import Optional, Union, List

cur_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
logger = logging.getLogger(__name__)


def generate_id() -> str:
    """
    generate a model id
    :return:
    """
    return str(time.time())


def get_project_root_path() -> str:
    project_path = os.getcwd()
    max_depth = 10  # 最大循环次数
    count = 0
    while not os.path.exists(os.path.join(project_path, 'README.md')):
        project_path = os.path.split(project_path)[0]
        count += 1
        if count > max_depth:  # 超出最大循环次数
            raise Exception('Could not find project root directory.')
    return project_path


def check_log_path():
    log_path = os.path.join(get_project_root_path(), 'log')
    if not os.path.exists(log_path):
        os.makedirs(log_path)


def get_cache_path():
    return f"{get_project_root_path()}/data"


def get_md5(dic: dict):
    return hashlib.md5(str(dic).encode("utf-8")).hexdigest()


def is_equals(dic1: dict, dic2: dict):
    return hashlib.md5(str(dic1).encode("utf-8")).hexdigest() == hashlib.md5(str(dic2).encode("utf-8")).hexdigest()


def enable_log():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
