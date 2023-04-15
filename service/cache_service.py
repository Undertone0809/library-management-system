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
# utils.enable_log()


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
    queried_data_list: List[dict] = []
    cache_models: List[dict] = cache[model.__name__]
    for cache_model in cache_models:
        for value in model.__dict__.values():
            if value and value in cache_model.values():
                queried_data_list.append(cache_model)
                break
    return queried_data_list


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
                logger.debug(f"[query_single_model_data] {cache_model}")
                return cache_model
    return None


def edit_model_data(model: BaseModel) -> List[dict]:
    queried_model = query_single_model_data(model)
    cache_models = get_all_model_data(type(model))
    logger.debug(f"[edit_model_data] original: {cache_models}")
    cache_models = [model.__dict__ if utils.is_equals(queried_model, cache_model) else cache_model for cache_model in
                    cache_models]
    logger.debug(f"[edit_model_data] modified: {cache_models}")
    cache[model.__name__] = cache_models
    return cache_models


def remove_model_data(model: BaseModel) -> List[dict]:
    queried_model = query_single_model_data(model)
    cache_models = get_all_model_data(type(model))
    while queried_model in cache_models:
        cache_models.remove(queried_model)
    cache[model.__name__] = cache_models
    return cache_models


def test():
    book = Book("good book", author="Jack")
    # cache['Book'] = [book.__dict__]
    # append_model_data(book)
    # print(cache['Book'])

    # print(query_models_data(book))

    # edit_model_data(book)

    remove_model_data(book)


# test()
