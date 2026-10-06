"""Тесты проекта 3 — «Плейлист на вечеринку» (`itertools`)."""

import itertools
import typing as tp

import pytest
from project03_party_playlist import double, intro_then_songs, loop, warmup, with_ads


def test_loop_is_infinite() -> None:
    assert list(itertools.islice(loop(["a", "b"]), 5)) == ["a", "b", "a", "b", "a"]


def test_warmup_repeats_when_n_longer_than_playlist() -> None:
    assert warmup(["a", "b", "c"], 5) == ["a", "b", "c", "a", "b"]


def test_warmup_shorter_than_playlist() -> None:
    assert warmup(["a", "b", "c"], 2) == ["a", "b"]


def test_with_ads_is_generator_function() -> None:
    import inspect

    assert inspect.isgeneratorfunction(with_ads)


def test_with_ads_inserts_after_every_n() -> None:
    stream = with_ads(["s1", "s2"], "AD", 2)
    assert list(itertools.islice(stream, 5)) == ["s1", "s2", "AD", "s1", "s2"]


def test_with_ads_every_one() -> None:
    stream = with_ads(["x", "y"], "AD", 1)
    assert list(itertools.islice(stream, 4)) == ["x", "AD", "y", "AD"]


def test_double_gives_independent_iterators() -> None:
    left, right = double([1, 2, 3])
    assert next(left) == 1
    assert next(right) == 1
    assert list(left) == [2, 3]
    assert list(right) == [2, 3]


def test_intro_then_songs_concatenates() -> None:
    assert list(intro_then_songs(["intro"], ["a", "b"])) == ["intro", "a", "b"]


def test_intro_then_songs_is_lazy() -> None:
    pulled: list[int] = []

    def songs() -> tp.Iterator[int]:
        for number in (1, 2):
            pulled.append(number)
            yield number

    combined = intro_then_songs(["intro"], songs())
    assert next(combined) == "intro"
    assert pulled == []  # второй источник ещё не тронут
    assert list(combined) == [1, 2]
