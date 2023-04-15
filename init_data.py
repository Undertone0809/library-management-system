# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 14:22
# @Author  : Zeeland
# @File    : init_data.py
# @Software: PyCharm

from model.book import Book
from service import cache_service


def init():
    cache_service.append_model_data(Book("Book1", "Jack", "PK publisher", "2023-4-5"))
    cache_service.append_model_data(Book("Book2", "Tom", "HK publisher", "2000-4-5"))
    cache_service.append_model_data(Book("Book3", "Jackson", "SH publisher", "1970-4-5"))


if __name__ == '__main__':
    init()
