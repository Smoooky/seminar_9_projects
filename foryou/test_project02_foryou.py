"""Тесты проекта 2 — «Рекомендации для тебя» (генераторы и ленивый конвейер)."""

import inspect
import typing as tp

import pytest
from project02_foryou import Clip, scored, top_titles, viral

CLIPS: list[Clip] = [
    {"title": "cats", "views": 10, "likes": 1},
    {"title": "skate", "views": 100, "likes": 3},
    {"title": "lofi", "views": 50, "likes": 20},
    {"title": "dance", "views": 100, "likes": 0},
]


def test_viral_is_generator_function() -> None:
    assert inspect.isgeneratorfunction(viral)


def test_scored_is_generator_function() -> None:
    assert inspect.isgeneratorfunction(scored)


def test_viral_filters_by_views() -> None:
    titles = [clip["title"] for clip in viral(CLIPS, 50)]
    assert titles == ["skate", "lofi", "dance"]


def test_scored_computes_rank() -> None:
    assert list(scored(CLIPS)) == [
        ("cats", 20),
        ("skate", 130),
        ("lofi", 250),
        ("dance", 100),
    ]


def test_viral_is_lazy() -> None:
    seen: list[int] = []

    def source() -> tp.Iterator[Clip]:
        for index in range(100):
            seen.append(index)
            yield {"title": str(index), "views": index, "likes": 0}

    gen = viral(source(), 50)
    assert seen == []  # тело генератора ещё не выполнялось
    assert next(gen)["views"] == 50
    assert seen == list(range(51))  # прочитали ровно до первого совпадения


def test_top_titles_keeps_stream_order_and_limits() -> None:
    # вирусные в порядке потока: skate(130), lofi(250), dance(100) — берём два
    assert top_titles(CLIPS, 50, 2) == ["skate", "lofi"]


def test_top_titles_stops_early_on_infinite_source() -> None:
    def endless() -> tp.Iterator[Clip]:
        while True:
            yield {"title": "x", "views": 1000, "likes": 1}

    assert top_titles(endless(), 0, 3) == ["x", "x", "x"]


def test_generator_is_one_shot() -> None:
    gen = viral(CLIPS, 0)
    first = list(gen)
    second = list(gen)
    assert first == CLIPS
    assert second == []


def test_scored_does_not_mutate_source() -> None:
    before = [dict(clip) for clip in CLIPS]
    list(scored(CLIPS))
    assert CLIPS == before
