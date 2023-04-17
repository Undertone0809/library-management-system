# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 23:24
# @Author  : Zeeland
# @File    : menu_service.py
# @Software: PyCharm

import logging
from model.book import Book
from rich.console import Console
from rich.table import Column, Table
from typing import Callable, Optional, List, Union
from service import book_service

console = Console()


def base_menu():
    console.print("Welcome to Library Management System")
    console.print("1. :green_book:Show Book")
    console.print("2. :toolbox:Query Book")
    console.print("3. :seat:Add Book")
    console.print("4. :dizzy:Edit Book")
    console.print("5. :shit:Remove Book")

    while True:
        choice = input("Please enter a number between 1 and 5: ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            break
        print("Invalid input, please try again.")

    _choose_func(int(choice))


def _choose_func(options):
    funcdic = {
        1: lambda: show_all_menu(),
        2: lambda: query_menu(),
        3: lambda: add_menu(),
        4: lambda: edit_menu(),
        5: lambda: remove_menu(),
    }
    return funcdic[options]()


def show_all_menu():
    books = book_service.show_all_books()
    _render_books_table(books)
    base_menu()


def query_menu():
    book_name = input("[Optional] Please enter book name:")
    author = input("[Optional] Please enter author:")
    publisher = input("[Optional] Please enter publisher:")
    books = book_service.query_books(book_name, author, publisher)
    _render_books_table(books)
    base_menu()


def add_menu():
    book_name = input("[Optional] Please enter book name:")
    author = input("[Optional] Please enter author:")
    publisher = input("[Optional] Please enter publisher:")
    publish_time = input("[Optional] Please enter publish time:")
    books = book_service.add_book(book_name, author, publisher, publish_time)
    _render_books_table(books)
    base_menu()


def edit_menu():
    book_name = input("[Edit Book] Please enter book name you want to edit:")
    book = book_service.query_single_book(book_name)
    _render_books_table([book])
    console.print(":grinning: Edit Your Book Here:")
    author = input("[Optional] Please enter author:")
    publisher = input("[Optional] Please enter publisher:")
    publish_time = input("[Optional] Please enter publish time:")
    book = book_service.edit_book(book_name, author, publisher, publish_time)
    _render_books_table([book])
    base_menu()


def remove_menu():
    book_name = input("[Optional] Please enter book name:")
    books = book_service.remove_book(book_name)
    _render_books_table(books)
    base_menu()


def _render_books_table(books: List[dict]):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("author", justify="center")
    table.add_column("id", style="dim", justify="center")
    table.add_column("book name", justify="center")
    table.add_column("public time", justify="center")
    table.add_column("publisher", justify="center")

    for book in books:
        table.add_row(*tuple(i for j in zip(book.values()) for i in j))
    console.print(table)
