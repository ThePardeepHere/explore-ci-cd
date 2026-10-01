from dataclasses import dataclass
from typing import List


# Passing marks for a subject.
PASSING_MARKS = 40

# Maximum marks possible for a subject.
MAX_MARKS = 100


@dataclass
class Student:
    """
    Represents a student in a school or college.

    Attributes:
        student_id: Unique ID of the student.
        name: Name of the student.
        age: Age of the student.
        course: Course or class of the student.
        marks: List of marks obtained in subjects.
    """

    student_id: int
    name: str
    age: int
    course: str
    marks: List[int]


def validate_student(student: Student) -> None:
    """
    Validate student information.

    Raises:
        ValueError: If any student information is invalid.
    """

    # Student ID must be greater than zero.
    if student.student_id <= 0:
        raise ValueError("Student ID must be positive")

    # Student name cannot be empty.
    if not student.name.strip():
        raise ValueError("Student name cannot be empty")

    # Student age must be realistic.
    if student.age <= 0 or student.age > 100:
        raise ValueError("Student age must be between 1 and 100")

    # Course/class cannot be empty.
    if not student.course.strip():
        raise ValueError("Course cannot be empty")

    # A student should have at least one subject mark.
    if not student.marks:
        raise ValueError("Student must have at least one subject")

    # Every mark must be between 0 and 100.
    for mark in student.marks:
        if mark < 0 or mark > MAX_MARKS:
            raise ValueError("Marks must be between 0 and 100")


def calculate_total_marks(student: Student) -> int:
    """
    Calculate the total marks obtained by a student.

    Args:
        student: Student whose marks need to be calculated.

    Returns:
        Total marks obtained.
    """

    validate_student(student)

    return sum(student.marks)


def calculate_percentage(student: Student) -> float:
    """
    Calculate the student's percentage.

    Args:
        student: Student whose percentage needs to be calculated.

    Returns:
        Percentage obtained by the student.
    """

    validate_student(student)

    total_marks = calculate_total_marks(student)
    maximum_marks = len(student.marks) * MAX_MARKS

    return (total_marks / maximum_marks) * 100


def calculate_grade(student: Student) -> str:
    """
    Calculate the student's grade based on percentage.

    Grade rules:

        A: 90 or above
        B: 75 to 89
        C: 60 to 74
        D: 40 to 59
        F: Below 40

    Args:
        student: Student whose grade needs to be calculated.

    Returns:
        Grade as a string.
    """

    percentage = calculate_percentage(student)

    if percentage >= 90:
        return "A"

    if percentage >= 75:
        return "B"

    if percentage >= 60:
        return "C"

    if percentage >= 40:
        return "D"

    return "F"


def is_passed(student: Student) -> bool:
    """
    Check whether the student has passed all subjects.

    A student passes only when every subject has
    marks greater than or equal to PASSING_MARKS.

    Args:
        student: Student whose result needs to be checked.

    Returns:
        True if the student passed all subjects.
        False otherwise.
    """

    validate_student(student)

    return all(mark >= PASSING_MARKS for mark in student.marks)


def get_top_students(
    students: List[Student],
    minimum_percentage: float = 80,
) -> List[Student]:
    """
    Return students whose percentage meets the given threshold.

    Args:
        students: List of students.
        minimum_percentage: Minimum percentage required.

    Returns:
        List of students meeting the percentage requirement.
    """

    for student in students:
        validate_student(student)

    return [
        student
        for student in students
        if calculate_percentage(student) >= minimum_percentage
    ]


def generate_result_report(
    students: List[Student],
) -> List[dict]:
    """
    Generate a result report for all students.

    The report contains:

        - Student ID
        - Student name
        - Course
        - Total marks
        - Percentage
        - Grade
        - Pass/Fail status

    Args:
        students: List of students.

    Returns:
        List of dictionaries containing result information.
    """

    report = []

    for student in students:
        report.append(
            {
                "student_id": student.student_id,
                "name": student.name,
                "course": student.course,
                "total_marks": calculate_total_marks(student),
                "percentage": calculate_percentage(student),
                "grade": calculate_grade(student),
                "passed": is_passed(student),
            }
        )

    return report


# This code runs only when main.py is executed directly.
#
# When test_main.py imports functions from main.py,
# this block will NOT execute.
if __name__ == "__main__":

    # Sample students.
    students = [
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

    print("Student Result Report")
    print("-" * 40)

    # Generate the result report.
    report = generate_result_report(students)

    # Display each student's result.
    for student in report:
        print(
            f"{student['name']}: "
            f"{student['percentage']:.2f}% | "
            f"Grade: {student['grade']} | "
            f"Passed: {student['passed']}"
        )

    # Find students with 80% or more.
    top_students = get_top_students(students)

    print("\nTop Students")
    print("-" * 40)

    for student in top_students:
        print(student.name)