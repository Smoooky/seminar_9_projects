"""Тесты проекта 4 — «Чат-копилка» (`send`)."""

import inspect

import pytest
from project04_tip_jar import jar


def test_jar_is_generator_function() -> None:
    assert inspect.isgeneratorfunction(jar)


def test_priming_returns_empty_dict() -> None:
    assert next(jar()) == {}


def test_send_counts_donations() -> None:
    gen = jar()
    assert next(gen) == {}
    assert gen.send("аня") == {"аня": 1}
    assert gen.send("босс") == {"аня": 1, "босс": 1}
    assert gen.send("аня") == {"аня": 2, "босс": 1}


def test_send_before_priming_raises() -> None:
    gen = jar()
    with pytest.raises(TypeError):
        gen.send("аня")


def test_snapshots_are_independent_copies() -> None:
    gen = jar()
    empty = next(gen)
    filled = gen.send("аня")
    assert empty == {}
    assert filled == {"аня": 1}
    assert empty is not filled


def test_send_none_finishes_generator() -> None:
    gen = jar()
    next(gen)
    gen.send("аня")
    with pytest.raises(StopIteration):
        gen.send(None)
    with pytest.raises(StopIteration):
        next(gen)


def test_jar_is_one_shot() -> None:
    gen = jar()
    next(gen)
    assert gen.send("x") == {"x": 1}
    with pytest.raises(StopIteration):
        gen.send(None)
    assert list(gen) == []
