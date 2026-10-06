"""Тесты проекта 1 — «Думскролл» (классы-итераторы)."""

import itertools

import pytest
from project01_doomscroll import Feed, FeedCursor, take


def test_feed_is_iterable_but_not_iterator() -> None:
    # каждый iter(feed) — новый обход, поэтому объекты разные
    feed = Feed(["a", "b"])
    assert iter(feed) is not iter(feed)


def test_feed_yields_all_items() -> None:
    assert list(Feed(["a", "b", "c"])) == ["a", "b", "c"]


def test_cursor_returns_self_from_iter() -> None:
    cursor = iter(Feed(["a"]))
    assert iter(cursor) is cursor


def test_cursor_type_is_feed_cursor() -> None:
    assert isinstance(iter(Feed(["a"])), FeedCursor)


def test_cursor_exhausts_with_stop_iteration() -> None:
    cursor = iter(Feed(["a"]))
    assert next(cursor) == "a"
    with pytest.raises(StopIteration):
        next(cursor)


def test_exhausted_cursor_does_not_revive() -> None:
    cursor = iter(Feed(["a", "b"]))
    assert list(cursor) == ["a", "b"]
    assert list(cursor) == []


def test_two_cursors_are_independent() -> None:
    feed = Feed(["a", "b", "c"])
    first, second = iter(feed), iter(feed)
    assert next(first) == "a"
    assert next(second) == "a"
    assert list(first) == ["b", "c"]
    assert list(second) == ["b", "c"]


def test_feed_copies_input() -> None:
    source = ["a", "b"]
    feed = Feed(source)
    source.append("c")
    assert list(feed) == ["a", "b"]


def test_take_limits() -> None:
    assert take(Feed(["a", "b", "c"]), 2) == ["a", "b"]


def test_take_works_on_infinite_source() -> None:
    # islice берёт ровно 3 элемента и не пытается исчерпать источник
    assert take(itertools.count(10), 3) == [10, 11, 12]


def test_take_more_than_available() -> None:
    assert take(Feed(["a"]), 5) == ["a"]
