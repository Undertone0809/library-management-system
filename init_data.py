# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 14:22
# @Author  : Zeeland
# @File    : init_data.py
# @Software: PyCharm

import utils
import faker
from datetime import datetime
from model.book import Book
from service import cache_service


def init():
    f = faker.Faker('en_US')

    for i in range(5):
        name = f.text(max_nb_chars=30)
        author = f.name()
        publisher = f.company()
        public_time = f.date_between(start_date='-10y', end_date='today')
        public_time_str = datetime.strftime(public_time, '%Y-%m-%d')

        cache_service.append_model_data(Book(name, author, publisher, public_time_str))


if __name__ == '__main__':
    utils.enable_log()
    init()
