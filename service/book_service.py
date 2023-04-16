# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 14:48
# @Author  : Zeeland
# @File    : book_service.py
# @Software: PyCharm

import logging
from model.base_model import BaseModel
from model.book import Book
from service import cache_service
from typing import Optional, List, Union

__all__ = ['show_all_books', 'add_book', 'query_books', 'query_single_book']


def show_all_books() -> Optional[List[dict]]:
    return cache_service.get_all_model_data(Book)


def add_book(name: Optional[str] = None, author: Optional[str] = None, publisher: Optional[str] = None,
             public_time: Optional[str] = None) -> Optional[List[dict]]:
    book = Book(name, author, publisher, public_time)
    return cache_service.append_model_data(book)


def query_books(name: Optional[str] = None, author: Optional[str] = None, publisher: Optional[str] = None,
                public_time: Optional[str] = None) -> List[dict]:
    book = Book(name, author, publisher, public_time)
    return cache_service.query_models_data(book)


def query_single_book(name: Optional[str] = None, author: Optional[str] = None, publisher: Optional[str] = None,
                      public_time: Optional[str] = None) -> Optional[dict]:
    book = Book(name, author, publisher, public_time)
    return cache_service.query_single_model_data(book)


def edit_book(name: Optional[str] = None, author: Optional[str] = None, publisher: Optional[str] = None,
              public_time: Optional[str] = None) -> dict:
    book = Book(name, author, publisher, public_time)
    return cache_service.edit_model_data(book)


def remove_book(name: Optional[str] = None, author: Optional[str] = None, publisher: Optional[str] = None,
                public_time: Optional[str] = None) -> Optional[List[dict]]:
    book = Book(name, author, publisher, public_time)
    return cache_service.remove_model_data(book)
