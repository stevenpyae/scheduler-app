from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    class_size = models.PositiveIntegerField() # Number of students the teacher can handle
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

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