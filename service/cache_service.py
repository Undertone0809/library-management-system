# -*- coding: utf-8 -*-
# @Time    : 2023/4/12 12:13
# @Author  : Zeeland
# @File    : cache_service.py
# @Software: PyCharm

import utils
import logging
from model.book import Book
from model.base_model import BaseModel
from cushy_storage import CushyDict
from typing import Union, Optional, List

logger = logging.getLogger(__name__)
cache = CushyDict(utils.get_cache_path())


def _check_model(model: type(BaseModel)):
    """
    Initializes the data space, otherwise raises KeyError
    """
    if model.__name__ not in cache:
        cache[model.__name__] = []


def get_all_model_data(model_type: type(BaseModel)) -> List[dict]:
    _check_model(model_type)
    logger.debug(f"[get_all_model_data] {cache[model_type.__name__]}")
    return cache[model_type.__name__]


def append_model_data(model: BaseModel) -> List[dict]:
    """
    Add a data after the original data, return all data
    :param model:
    :return:
    """
    _check_model(type(model))
    ret: List[dict] = cache[model.__name__]
    ret.append(model.__dict__)
    cache[model.__name__] = ret
    logger.debug(cache[model.__name__])
    return cache[model.__name__]


def query_models_data(model: BaseModel) -> Optional[List[dict]]:
    ret: List[dict] = []
    cache_models: List[dict] = cache[model.__name__]
    for cache_model in cache_models:
        for value in model.__dict__.values():
            if value and value in cache_model.values():
                ret.append(cache_model)
                break

    return ret

def query_single_model_data(model: BaseModel) -> Optional[dict]:
    """
    Query single model data. If more than one data exists, only
    the first query is returned.
    :param model: For example, you can input a book instance
    :return:
        Returns dict type of instance like as follows:
        {
            'author': None,
            'id': '1681551363.9869192',
            'name': 'my_book',
            'public_time': None,
            'publisher': None
        }
        If there is no result, none is returned.

    """
    cache_models: List[dict] = cache[model.__name__]
    for cache_model in cache_models:
        for value in model.__dict__.values():
            if value and value in cache_model.values():
                return cache_model
    return None


def edit_model(model: BaseModel) -> List[dict]:

    res = query_single_model_data(model)


def remove_model(model: BaseModel) -> List[dict]:
    # query model data firstly
    pass


def test():
    book = Book("my_book")
    # cache['Book'] = [book.__dict__]
    # append_model_data(book)
    # print(cache['Book'])
    # print(list(book.__dict__.values()))
    print(query_models_data(book))


test()
