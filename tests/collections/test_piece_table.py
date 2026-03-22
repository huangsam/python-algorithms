import pytest

from algorithms.collections.piece_table import PieceTable


@pytest.mark.collections
def test_piece_table_init():
    pt = PieceTable("Hello")
    assert pt.get_text() == "Hello"


@pytest.mark.collections
def test_piece_table_insert():
    pt = PieceTable("Hello")
    pt.insert(5, " World")
    assert pt.get_text() == "Hello World"


@pytest.mark.collections
def test_piece_table_insert_middle():
    pt = PieceTable("Hello World")
    pt.insert(6, "Beautiful ")
    assert pt.get_text() == "Hello Beautiful World"


@pytest.mark.collections
def test_piece_table_delete():
    pt = PieceTable("Hello Beautiful World")
    pt.delete(6, 10)
    assert pt.get_text() == "Hello World"


@pytest.mark.collections
def test_piece_table_delete_start():
    pt = PieceTable("Hello World")
    pt.delete(0, 6)
    assert pt.get_text() == "World"


@pytest.mark.collections
def test_piece_table_complex():
    pt = PieceTable("Original")
    pt.insert(8, " text")
    pt.insert(0, "The ")
    pt.delete(4, 9)
    assert pt.get_text() == "The text"
