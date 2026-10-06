"""Проект 2. «Рекомендации для тебя» — генераторные функции и выражения.

Тема лекции 9: генераторная функция не выполняет тело при вызове, генератор
ленив и одноразов, а конвейер из генераторов не держит промежуточные данные
в памяти.

Клип — это словарь с ключами `"title"`, `"views"`, `"likes"`. Конвейер
строится из маленьких ленивых звеньев: отфильтровать вирусные, посчитать
«вирусный балл», взять верхушку.

Помни: `viral` и `scored` должны быть **генераторными функциями**
(`inspect.isgeneratorfunction`), а не возвращать собранный список. Иначе
на большом источнике конвейер съест память — ровно та проблема, которую
генераторы и решают.
"""

import itertools
import typing as tp

Clip = dict[str, tp.Any]


def viral(clips: tp.Iterable[Clip], min_views: int) -> tp.Iterator[Clip]:
    """Лениво отдавать клипы, у которых `views >= min_views`.

    Должна быть генераторной функцией: `yield` внутри цикла `for`.
    """
    raise NotImplementedError("Implement me")


def scored(clips: tp.Iterable[Clip]) -> tp.Iterator[tuple[str, int]]:
    """Лениво отдавать пары `(title, views + 10 * likes)`.

    «Вирусный балл» намеренно перевешивает лайки над просмотрами.
    Должна быть генераторной функцией.
    """
    raise NotImplementedError("Implement me")


def top_titles(clips: tp.Iterable[Clip], min_views: int, limit: int) -> list[str]:
    """Заголовки первых `limit` клипов, прошедших порог `min_views`.

    Порядок — как в потоке, без глобальной сортировки: сортировка потребовала
    бы прочитать весь источник и убила бы ленивость (для бесконечного потока
    она вообще не завершится). Собери конвейер `scored(viral(...))` и обрежь
    его `itertools.islice`.
    """
    raise NotImplementedError("Implement me")
