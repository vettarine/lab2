#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os #модуль служащий для работы с ОС
import sys #модуль предоставляющий доступ к функциям исп интерпретатором Питона


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings') #переменная окружения
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc: #ошибка если питон не находит модуль в импорте
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv) #argv - список аргументов командной строки


if __name__ == '__main__':
    main()
