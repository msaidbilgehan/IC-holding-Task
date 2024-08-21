from django.db import models



class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    time_start = models.DateTimeField(auto_now_add=True)


class TaskCompletionLog(models.Model):
    task_assignment = models.ForeignKey(
        TaskAssignment, on_delete=models.CASCADE
    )
    time_start = models.DateTimeField()
    time_completed = models.DateTimeField(null=True, blank=True)
