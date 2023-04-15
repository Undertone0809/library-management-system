# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 21:41
# @Author  : Zeeland
# @File    : user_service.py
# @Software: PyCharm

from typing import Optional, List
from service import cache_service
from model.user import User


def show_all_user() -> Optional[List[dict]]:
    return cache_service.get_all_model_data(User)
