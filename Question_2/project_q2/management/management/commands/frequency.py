from django.core.management.base import BaseCommand
from django.db.models import Count
from management.models import TaskCompletionLog
from django.utils import timezone


class Command(BaseCommand):
    help = 'Person-Task frequency calculation'

    def add_arguments(self, parser):
        # Adding a command line option to specify the person's ID
        parser.add_argument(
            'range_day',
            type=int,
            default=30,
            help='The range of days to calculate the frequency, default is 30 days'
        )
        parser.add_argument(
            'human_readable',
            type=int,
            default=0,
            help='Output in human readable format'
        )

    def handle(self, *args, **options):
        frequencies = self.calculate_frequencies(range_day=options['range_day'])
        if frequencies:
            # self.stdout.write(f"{frequencies}")
            if options['human_readable'] == 1:
                for freq in frequencies:
                    self.stdout.write(
                        f"Person ID: {freq['task_assignment__person__id']}, Task ID: {freq['task_assignment__task__id']}, Frequency: {freq['frequency']}"
                    )
            else:
                self.stdout.write(
                    f"{frequencies}"
                )
        else:
            self.stdout.write("No task completions found in the specified range.")


    def calculate_frequencies(self, range_day: int):
        range_day_datetime = timezone.now() - timezone.timedelta(days=range_day)
        return TaskCompletionLog.objects.filter(
            time_completed__gte=range_day_datetime
        ).values(
            'task_assignment__person__id',
            'task_assignment__task__id'
        ).annotate(
            frequency=Count('id')
        ).order_by(
            'task_assignment__person__id',
            'task_assignment__task__id'
        )
