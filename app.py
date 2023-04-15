import logging
from rich.console import Console
from rich.table import Column, Table
from service import menu_service

logger = logging.getLogger(__name__)
console = Console()


def enable_log():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class LibraryManagementSystemApplication:
    def run(self):
        menu_service.base_menu()


def main():
    enable_log()
    app = LibraryManagementSystemApplication()
    app.run()


if __name__ == '__main__':
    main()
