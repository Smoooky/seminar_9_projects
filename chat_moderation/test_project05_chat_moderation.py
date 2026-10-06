"""Тесты проекта 5 — «Модерация чата» (`throw`, `close`)."""

import inspect

import pytest
from project05_chat_moderation import moderator


def test_moderator_is_generator_function() -> None:
    assert inspect.isgeneratorfunction(moderator)


def test_priming_returns_zero() -> None:
    assert next(moderator()) == 0


def test_send_counts_messages() -> None:
    gen = moderator()
    assert next(gen) == 0
    assert gen.send("привет") == 1
    assert gen.send("как дела") == 2


def test_throw_value_error_resets_counter() -> None:
    gen = moderator()
    next(gen)
    gen.send("a")
    gen.send("b")
    # исключение поймано внутри, поэтому throw возвращает следующее значение
    assert gen.throw(ValueError("плохое слово")) == 1
    assert gen.send("c") == 2  # без сброса было бы 3


def test_throw_unknown_exception_finishes() -> None:
    gen = moderator()
    next(gen)
    gen.send("a")
    with pytest.raises(RuntimeError):
        gen.throw(RuntimeError("всё сломалось"))
    with pytest.raises(StopIteration):
        next(gen)


def test_close_prints_stop(
    capsys: pytest.CaptureFixture[str],
) -> None:
    gen = moderator()
    next(gen)
    gen.send("a")
    gen.close()
    assert "stop" in capsys.readouterr().out


def test_closed_generator_is_dead() -> None:
    gen = moderator()
    next(gen)
    gen.close()
    with pytest.raises(StopIteration):
        next(gen)
