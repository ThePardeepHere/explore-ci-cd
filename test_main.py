import pytest

from main import (
    Student,
    validate_student,
    calculate_total_marks,
    calculate_percentage,
    calculate_grade,
    is_passed,
    get_top_students,
    generate_result_report,
)


@pytest.fixture
def student():
    """
    Create a sample student for testing.
    """

    return Student(
        student_id=1,
        name="Pardeep",
        age=25,
        course="MCA",
        marks=[90, 85, 92, 88, 95],
    )


@pytest.fixture
def students():
    """
    Create multiple students for testing.
    """

    return [
        Student(
            student_id=1,
            name="Pardeep",
            age=25,
            course="MCA",
            marks=[90, 85, 92, 88, 95],
        ),
        Student(
            student_id=2,
            name="Rahul",
            age=22,
            course="BCA",
            marks=[75, 80, 72, 78, 82],
        ),
        Student(
            student_id=3,
            name="Aman",
            age=21,
            course="BCA",
            marks=[35, 45, 50, 38, 42],
        ),
    ]


def test_student_validation(student):
    """
    Valid student should not raise an exception.
    """

    validate_student(student)


def test_total_marks(student):
    """
    Verify total marks calculation.
    """

    assert calculate_total_marks(student) == 450


def test_percentage(student):
    """
    Verify percentage calculation.
    """

    assert calculate_percentage(student) == 90


def test_grade_a(student):
    """
    Student with 90% should receive grade A.
    """

    assert calculate_grade(student) == "A"


def test_student_passed(student):
    """
    Student should pass when all subjects
    have marks >= 40.
    """

    assert is_passed(student) is True


def test_student_failed():
    """
    Student should fail if any subject has
    marks below 40.
    """

    student = Student(
        student_id=2,
        name="Aman",
        age=21,
        course="BCA",
        marks=[35, 45, 50, 38, 42],
    )

    assert is_passed(student) is False


def test_grade_b():
    """
    Verify grade B calculation.
    """

    student = Student(
        student_id=2,
        name="Rahul",
        age=22,
        course="BCA",
        marks=[75, 80, 72, 78, 82],
    )

    assert calculate_grade(student) == "B"


def test_top_students(students):
    """
    Verify that students with 80% or more
    are returned.
    """

    result = get_top_students(students)

    assert len(result) == 1
    assert result[0].name == "Pardeep"


def test_custom_percentage_threshold(students):
    """
    Verify custom percentage threshold.
    """

    result = get_top_students(
        students,
        minimum_percentage=70,
    )

    assert len(result) == 2


def test_result_report(students):
    """
    Verify the generated result report.
    """

    report = generate_result_report(students)

    assert len(report) == 3

    assert report[0]["name"] == "Pardeep"
    assert report[0]["total_marks"] == 450
    assert report[0]["percentage"] == 90
    assert report[0]["grade"] == "A"
    assert report[0]["passed"] is True


def test_invalid_student_id():
    """
    Student ID must be positive.
    """

    student = Student(
        student_id=0,
        name="Pardeep",
        age=25,
        course="MCA",
        marks=[90, 80],
    )

    with pytest.raises(ValueError):
        validate_student(student)


def test_empty_student_name():
    """
    Student name cannot be empty.
    """

    student = Student(
        student_id=1,
        name="",
        age=25,
        course="MCA",
        marks=[90, 80],
    )

    with pytest.raises(ValueError):
        validate_student(student)


def test_invalid_marks():
    """
    Marks cannot be greater than 100.
    """

    student = Student(
        student_id=1,
        name="Pardeep",
        age=25,
        course="MCA",
        marks=[90, 105],
    )

    with pytest.raises(ValueError):
        validate_student(student)


def test_empty_marks():
    """
    Student must have at least one subject.
    """

    student = Student(
        student_id=1,
        name="Pardeep",
        age=25,
        course="MCA",
        marks=[],
    )

    with pytest.raises(ValueError):
        validate_student(student)