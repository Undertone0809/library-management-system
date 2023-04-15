# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 23:24
# @Author  : Zeeland
# @File    : menu_service.py
# @Software: PyCharm

import logging
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
    print(books)

def query_menu():
    pass


def add_menu():
    pass


def edit_menu():
    pass


def remove_menu():
    pass


functions: List[Callable] = [show_all_menu, query_menu, add_menu, edit_menu, remove_menu]
