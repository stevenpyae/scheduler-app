#api/services/scheduling.py

def has_conflicting_students(student_queryset):
    """
    Returns True if any students in the given queryset are incompatible with each other.
    """
    student_list = list(student_queryset)  # Convert to list for indexing

    for i in range(len(student_list)):
        for j in range(i + 1, len(student_list)):
            student_a = student_list[i]
            student_b = student_list[j]
            if student_b in student_a.incompatible_students.all():
                return True
    return False
