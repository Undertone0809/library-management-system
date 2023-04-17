import utils
import logging
from service import menu_service

logger = logging.getLogger(__name__)


class LibraryManagementSystemApplication:
    def run(self):
        menu_service.base_menu()


def main():
    # utils.enable_log()
    app = LibraryManagementSystemApplication()
    app.run()


if __name__ == '__main__':
    main()
