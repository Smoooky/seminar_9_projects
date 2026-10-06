"""Тесты проекта 7 — «Автокомплит» (`itertools` и `yield from`)."""

import inspect
import typing as tp

import pytest
from project07_autocomplete import (
    flatten,
    matches,
    skip_until,
    suggest,
    take_prefix,
)


def test_flatten_is_generator_function() -> None:
    assert inspect.isgeneratorfunction(flatten)


def test_matches_is_generator_function() -> None:
    assert inspect.isgeneratorfunction(matches)


def test_flatten_concatenates_sources() -> None:
    assert list(flatten(["a"], ["b", "c"], "de")) == ["a", "b", "c", "d", "e"]


def test_flatten_no_sources() -> None:
    assert list(flatten()) == []


def test_flatten_is_lazy_across_sources() -> None:
    touched: list[str] = []

    def second() -> tp.Iterator[str]:
        touched.append("second")
        yield "b"

    gen = flatten(["a"], second())
    assert next(gen) == "a"
    assert touched == []  # второй источник ещё не тронут
    assert list(gen) == ["b"]


def test_matches_filters_case_insensitively() -> None:
    words = ["Аня", "Ананас", "Босс", "апельсин"]
    assert list(matches("ан", words)) == ["Аня", "Ананас"]


def test_matches_empty_query_returns_all() -> None:
    assert list(matches("", ["x", "y"])) == ["x", "y"]


def test_suggest_limits_across_banks() -> None:
    bank_one = ["аня", "анanas", "босс"]
    bank_two = ["антена", "ангел"]
    assert suggest("ан", bank_one, bank_two, limit=3) == ["аня", "анanas", "антена"]


def test_suggest_does_not_read_extra() -> None:
    read: list[str] = []

    def bank() -> tp.Iterator[str]:
        for word in ["аня", "аня2", "аня3", "аня4"]:
            read.append(word)
            yield word

    assert suggest("ан", bank(), limit=2) == ["аня", "аня2"]
    assert read == ["аня", "аня2"]  # третий элемент не читали


def test_skip_until_drops_through_value() -> None:
    assert list(skip_until(["a", "b", "c", "b"], "b")) == ["b", "c", "b"]


def test_skip_until_value_absent_gives_empty() -> None:
    assert list(skip_until(["a", "b"], "z")) == []


def test_take_prefix_stops_at_first_non_prefix() -> None:
    words = ["аня", "анanas", "босс", "ангел"]
    assert take_prefix(words, "ан") == ["аня", "анanas"]


def test_take_prefix_empty_when_first_word_mismatches() -> None:
    assert take_prefix(["босс", "аня"], "ан") == []
