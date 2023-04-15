# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 14:52
# @Author  : Zeeland
# @File    : base_model.py
# @Software: PyCharm

import hashlib


class BaseModel:
    __name__ = 'BaseModel'

    def query(self):
        pass

    def add(self):
        pass

    def edit(self):
        pass

    def remove(self):
        pass

    def md5(self):
        return hashlib.md5(str(self.__dict__).encode("utf-8")).hexdigest()
