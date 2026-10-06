"""Тесты проекта 6 — «Стрим чанками» (вторая форма `iter`)."""

import itertools
from collections.abc import Iterator

import pytest
from project06_stream_chunks import chunks, collect, until


def test_chunks_even_split() -> None:
    assert list(chunks("abcdef", 2)) == ["ab", "cd", "ef"]


def test_chunks_ragged_tail() -> None:
    assert list(chunks("abcde", 2)) == ["ab", "cd", "e"]


def test_chunks_empty_source() -> None:
    assert list(chunks("", 3)) == []


def test_chunks_size_larger_than_source() -> None:
    assert list(chunks("ab", 10)) == ["ab"]


def test_chunks_returns_iterator() -> None:
    result = chunks("abc", 1)
    assert iter(result) is result


def test_collect_same_as_list() -> None:
    assert collect("abcdefg", 3) == ["abc", "def", "g"]


def test_until_stops_at_sentinel() -> None:
    values: Iterator[int] = iter([1, 2, 3, 0, 9])

    def produce() -> int:
        return next(values)

    assert list(until(produce, 0)) == [1, 2, 3]


def test_until_sentinel_not_yielded() -> None:
    values = iter([1, 0])

    def produce() -> int:
        return next(values)

    assert 0 not in list(until(produce, 0))


def test_until_compares_with_equality_not_identity() -> None:
    # 1.0 == 1, поэтому sentinel срабатывает по первому же значению
    values: Iterator[float] = iter([1.0, 2.0, 3.0])

    def produce() -> float:
        return next(values)

    assert list(until(produce, 1)) == []


def test_until_with_object_sentinel() -> None:
    end = object()
    values: list[object] = ["a", "b", end]

    def produce() -> object:
        return values.pop(0)

    assert list(until(produce, end)) == ["a", "b"]
