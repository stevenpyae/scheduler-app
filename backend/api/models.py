from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    class_size = models.PositiveIntegerField() # Number of students the teacher can handle
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ String representation of the Teacher: Easier to identify the teacher """
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length = 10, choices=list('High', 'Low', 'Mid'))  # Priority level for scheduling 1 - Low, 5 - High

    incompatible_students = models.ManyToManyField(
        'self', 
        symmetrical=True, # This field allows a student to have a many-to-many relationship with other students 
        related_name='incompatible_with',
        blank=True
    )  # Students who cannot be in the same session

    def __str__(self):
        """ String representation of the student: Easier to identify the student """
        return self.name
    
    def clean(self): ## Does not work with .add() misuse
        """ Custom validation to ensure no student is incompatible with themselves """
        if self in self.incompatible_students.all():
            raise ValueError("A student cannot be incompatible with himself/herself.")

class Session(models.Model):
    """ Can Query like:  
    session.students.all() 
    student.sessions.all()
    teacher.sessions.all()
    """
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='sessions') # Each session is led by one teacher
    students = models.ManyToManyField(Student, related_name='sessions') # Many students can attend a session
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        """ String representation of the session: Easier to identify the session """
        return f"Session by {self.teacher.name} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"