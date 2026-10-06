"""Проект 3. «Плейлист на вечеринку» — модуль `itertools`.

Тема лекции 9: `itertools.cycle`, `islice`, `chain`, `tee` и разница между
бесконечным источником и ограничителем сверху.

Плейлист зацикливается, между треками вклинивается реклама, а ещё нужно
склеить интро с песнями и раздвоить один обход на два независимых.

Важно про ленивость: `chain` не трогает следующий источник, пока не исчерпан
предыдущий, а `tee` раздваивает обход ценой буферизации. `cycle` бесконечен —
его всегда нужно ограничивать `islice` или `takewhile`.
"""

import itertools
import typing as tp


def loop(playlist: tp.Sequence[str]) -> tp.Iterator[str]:
    """Бесконечный круговой обход плейлиста (`itertools.cycle`)."""
    raise NotImplementedError("Implement me")


def warmup(playlist: tp.Sequence[str], n: int) -> list[str]:
    """Первые `n` треков зацикленного плейлиста.

    Если `n` больше длины плейлиста — просто пойдёт по кругу.
    """
    raise NotImplementedError("Implement me")


def with_ads(
    playlist: tp.Sequence[str], ad: str, every: int
) -> tp.Iterator[str]:
    """Бесконечный поток: после каждых `every` треков вставить `ad`.

    Должна быть генераторной функцией. Пример для `["s1", "s2"]`,
    `ad="AD"`, `every=2`: `s1, s2, AD, s1, s2, AD, ...`
    """
    raise NotImplementedError("Implement me")


def double(iterable: tp.Iterable[str]) -> tuple[tp.Iterator[str], tp.Iterator[str]]:
    """Раздвоить один обход на два независимых (`itertools.tee`)."""
    raise NotImplementedError("Implement me")


def intro_then_songs(
    intro: tp.Iterable[str], playlist: tp.Iterable[str]
) -> tp.Iterator[str]:
    """Склеить интро и песни лениво (`itertools.chain`)."""
    raise NotImplementedError("Implement me")
