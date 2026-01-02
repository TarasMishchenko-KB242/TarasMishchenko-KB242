import pytest
from lab2 import students, addNewElement, deleteElement, updateElement

def setup_function():
    """Очищує список перед кожним тестом."""
    global students
    students.clear()

def test_add_student():
    addNewElement("Ivan", "111", "ivan@mail.com", "KB-22")
    assert len(students) == 1
    assert students[0]["name"] == "Ivan"

def test_sorting_on_add():
    addNewElement("Zak", "333", "zak@mail.com", "KB-22")
    addNewElement("Alex", "111", "alex@mail.com", "KB-22")
    # Alex має бути першим за алфавітом
    assert students[0]["name"] == "Alex"
    assert students[1]["name"] == "Zak"

def test_delete_student():
    addNewElement("Ivan", "111", "ivan@mail.com", "KB-22")
    result = deleteElement("Ivan")
    assert result is True
    assert len(students) == 0

def test_delete_non_existent():
    result = deleteElement("Unknown")
    assert result is False

def test_update_student():
    addNewElement("OldName", "111", "old@mail.com", "KB-1")
    updateElement("OldName", "NewName", "222", "new@mail.com", "KB-2")
    assert students[0]["name"] == "NewName"
    assert students[0]["phone"] == "222"
    assert len(students) == 1