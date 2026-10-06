"""Проект 1. «Думскролл» — классы-итераторы и протокол `__iter__`/`__next__`.

Тема лекции 9: различие между итерируемым и итератором, ручной протокол
обхода и одноразовость итератора.

`Feed` — это лента рекомендаций. Она **итерируемая**, но не итератор:
каждый `iter(feed)` должен возвращать **новый** обходчик, чтобы по одной
ленте можно было вести два независимых перебора.

`FeedCursor` — сам обходчик. Это **итератор**: у него есть состояние «где мы
сейчас», `__iter__` возвращает `self`, а `__next__` отдаёт следующий элемент
и возбуждает `StopIteration`, когда лента кончилась. Одноразовость — часть
контракта: исчерпанный курсор не оживает.

`take` умеет взять первые `n` элементов, не материализуя весь источник, —
именно для этого нужен `itertools.islice`.
"""

import itertools
from collections.abc import Iterable, Iterator


class Feed:
    """Лента рекомендаций: итерируемое, но не итератор."""

    def __init__(self, items: list[str] | tuple[str, ...] = ()) -> None:
        """Сохранить элементы ленты копией, а не ссылкой на чужой список."""
        raise NotImplementedError("Implement me")

    def __iter__(self) -> "FeedCursor":
        """Вернуть **новый** обходчик по ленте."""
        raise NotImplementedError("Implement me")


class FeedCursor:
    """Обходчик ленты: итератор с состоянием."""

    def __init__(self, items: list[str]) -> None:
        """Запомнить элементы и начать обход с нулевого индекса."""
        raise NotImplementedError("Implement me")

    def __iter__(self) -> "FeedCursor":
        """Итератор обязан возвращать из `__iter__` самого себя."""
        raise NotImplementedError("Implement me")

    def __next__(self) -> str:
        """Следующий элемент или `StopIteration`, если элементы кончились."""
        raise NotImplementedError("Implement me")


def take(iterable: Iterable[str], n: int) -> list[str]:
    """Первые `n` элементов, не читая источник дальше необходимого.

    Работает и с бесконечным источником вроде `itertools.count()`.
    Список руками не собирай циклом `for` — используй `itertools.islice`.
    """
    raise NotImplementedError("Implement me")
