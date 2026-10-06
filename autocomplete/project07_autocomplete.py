"""Проект 7. «Автокомплит» — `itertools` и `yield from`.

Тема лекции 9: `yield from` делегирует обход другому источнику, а
`chain`/`dropwhile`/`takewhile`/`islice` ограничивают и склеивают потоки,
не материализуя их.

Собираем автокомплит для поисковой строки:
- `flatten` склеивает несколько словарей в один поток;
- `matches` лениво выбирает слова с нужным префиксом;
- `suggest` берёт первые `limit` подсказок из нескольких банков;
- `skip_until` отбрасывает начало до слова `value` включительно;
- `take_prefix` забирает непрерывный блок слов с данным префиксом с начала.

`flatten` и `matches` обязаны быть генераторными функциями.
"""

import itertools
import typing as tp


def flatten(*sources: tp.Iterable[str]) -> tp.Iterator[str]:
    """Склеить источники в один поток, по порядку (через `yield from`)."""
    raise NotImplementedError("Implement me")


def matches(query: str, words: tp.Iterable[str]) -> tp.Iterator[str]:
    """Лениво отдавать слова, начинающиеся с `query` (без учёта регистра)."""
    raise NotImplementedError("Implement me")


def suggest(query: str, *banks: tp.Iterable[str], limit: int) -> list[str]:
    """Первые `limit` подсказок из всех банков по порядку.

    Банки склеивай `itertools.chain`, ограничивай `itertools.islice`, так
    чтобы лишние слова из банков не читались.
    """
    raise NotImplementedError("Implement me")


def skip_until(words: tp.Iterable[str], value: str) -> tp.Iterator[str]:
    """Отбросить слова до `value` включительно (`itertools.dropwhile`)."""
    raise NotImplementedError("Implement me")


def take_prefix(words: tp.Iterable[str], prefix: str) -> list[str]:
    """Непрерывный блок слов с префиксом `prefix` с самого начала.

    Как только встретилось слово без префикса — остановиться
    (`itertools.takewhile`).
    """
    raise NotImplementedError("Implement me")
