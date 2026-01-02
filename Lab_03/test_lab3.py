import pytest
from Student import Student
from StudentList import StudentList

def test_add_student():
    sl = StudentList()
    s = Student("Alex", "123", "a@m.com", "K-1")
    sl.add_student(s)
    assert len(sl.get_all()) == 1
    assert sl.get_all()[0].name == "Alex"

def test_sorting():
    sl = StudentList()
    sl.add_student(Student("Zoe", "1", "z@m.com", "1"))
    sl.add_student(Student("Alex", "2", "a@m.com", "2"))
    assert sl.get_all()[0].name == "Alex"
    assert sl.get_all()[1].name == "Zoe"

def test_delete():
    sl = StudentList()
    sl.add_student(Student("Bob", "1", "b@m.com", "1"))
    assert sl.delete_student("Bob") is True
    assert len(sl.get_all()) == 0