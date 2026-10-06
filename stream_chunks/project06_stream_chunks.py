"""Проект 6. «Стрим чанками» — вторая форма `iter(callable, sentinel)`.

Тема лекции 9: `iter(функция, sentinel)` зовёт функцию без аргументов и
отдаёт результаты, пока очередной не окажется **равен** sentinel'у. Сам
sentinel наружу не выходит, а сравнение идёт через `==` — не через `is`.

`chunks` режет строку на куски по `size` символов, как чтение файла порциями.
Хвост отдаётся как есть, даже если он короче `size`. Реализуй через
`io.StringIO` + `functools.partial` + `iter(read, "")`: `read(size)` читает
ровно `size` символов, а на исчерпании возвращает `""`.

`until` — обобщённая версия: итератор по результатам функции `produce`, пока
не встретится `sentinel`.
"""

import io
from collections.abc import Callable, Iterator
from functools import partial
from typing import TypeVar

T = TypeVar("T")


def chunks(source: str, size: int) -> Iterator[str]:
    """Лениво отдавать куски по `size` символов; хвост — как есть.

    Возвращает именно итератор (то, что вернул `iter(...)`), а не список.
    """
    raise NotImplementedError("Implement me")


def collect(source: str, size: int) -> list[str]:
    """Собрать все куски в список."""
    raise NotImplementedError("Implement me")


def until(produce: Callable[[], T], sentinel: T) -> Iterator[T]:
    """Итератор по вызовам `produce()`, пока результат не равен `sentinel`.

    Sentinel не должен попадать в результат. Сравнение — через `==`.
    """
    raise NotImplementedError("Implement me")
