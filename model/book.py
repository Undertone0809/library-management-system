# -*- coding: utf-8 -*-
# @Time    : 2023/4/12 11:21
# @Author  : Zeeland
# @File    : book.py
# @Software: PyCharm

import os
import time
from model.base_model import BaseModel
from typing import Optional, List, Union


def generate_id() -> str:
    """
    generate a model id
    :return:
    """
    return str(time.time())


class Book(BaseModel):
    __name__ = 'Book'

    def __init__(self, name: str, author: Optional[str] = None, publisher: Optional[str] = None,
                 public_time: Optional[str] = None, **kwargs):
        super().__init__()
        self.id = generate_id()
        self.name = name
        self.author = author
        self.publisher = publisher
        self.public_time = public_time

    def save(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    def add(self):
        pass
