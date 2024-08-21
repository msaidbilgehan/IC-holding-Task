from django.core.management.base import BaseCommand
from django.utils import timezone
import random

from management.models import Person, Task, TaskAssignment, TaskCompletionLog


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        # Create Persons
        persons = [
            Person(first_name=f'Person{i}', last_name=f'Lastname{i}') for i in range(10)]
        Person.objects.bulk_create(persons)

        # Create Tasks
        tasks = [
            Task(title=f'Task{i}', description=f'Description of Task{i}') for i in range(5)
        ]
        Task.objects.bulk_create(tasks)

        # Create TaskAssignments
        for person in Person.objects.all():
            for task in Task.objects.all():
                TaskAssignment.objects.create(person=person, task=task)

        # Create TaskCompletionLogs
        for assignment in TaskAssignment.objects.all():
            completion_date = timezone.now() - timezone.timedelta(days=random.randint(0, 30))
            TaskCompletionLog.objects.create(
                task_assignment=assignment,
                time_start=completion_date,
                time_completed=completion_date +
                timezone.timedelta(hours=random.randint(1, 5))
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded the database.'
        ))
