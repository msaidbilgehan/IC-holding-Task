from django.core.management.base import BaseCommand
from django.utils import timezone
import random

from management.models import Person, Task, TaskAssignment, TaskCompletionLog


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        # Create Persons
        # persons = [
        #     Person(first_name=f'Person{i}', last_name=f'Lastname{i}') for i in range(10)
        #     ]
        # Person.objects.bulk_create(persons)

        # Create Persons
        number_of_person = 4
        for i in range(number_of_person):
            Person.objects.get_or_create(
                first_name=f'Alfa{i}',
                last_name=f'Theta{i}'
            )
            self.stdout.write(self.style.SUCCESS(
                f'Created Person - {i}'
            ))

        # Create Tasks
        number_of_tasks = 5
        for i in range(number_of_tasks):
            Task.objects.get_or_create(
                title=f'Task{i}',
                description=f'Description of Task{i}'
            )
            self.stdout.write(self.style.SUCCESS(
                f'Created Task - {i}'
            ))

        # Create TaskAssignments
        number_of_assignments = 10
        for person in Person.objects.all():
            for i in range(number_of_assignments):
                for task in Task.objects.all():
                    # To randomize the task assignment
                    if random.randint(1, 5) != 1:
                        TaskAssignment.objects.create(person=person, task=task)
                        self.stdout.write(self.style.SUCCESS(
                            f'Assigned Task - {task.title} to {person.first_name} {person.last_name}'
                        ))

        # Create TaskCompletionLogs
        for assignment in TaskAssignment.objects.all():
            completion_date = timezone.now() - timezone.timedelta(days=random.randint(0, 30))
            TaskCompletionLog.objects.create(
                task_assignment=assignment,
                time_start=completion_date,
                time_completed=completion_date + timezone.timedelta(hours=random.randint(1, 7))
            )

            self.stdout.write(self.style.SUCCESS(
                f'Tasks completed by {assignment.person.first_name} {assignment.person.last_name} for {assignment.task.title}'
            ))

        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded the database.'
        ))
