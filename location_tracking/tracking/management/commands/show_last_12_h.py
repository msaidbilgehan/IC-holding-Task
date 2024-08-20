from django.core.management.base import BaseCommand
from django.utils.timezone import now
from tracking.models import LocationRecord
from datetime import timedelta


class Command(BaseCommand):
    help = 'Display all location data for a specific person in the last 12 hours'

    def add_arguments(self, parser):
        # Adding a command line option to specify the person's ID
        parser.add_argument(
            'person_id',
            type=int,
            default=1,
            help='ID of the person to retrieve locations for'
        )
        # Check the day before
        parser.add_argument(
            'day',
            type=int,
            default=0,
            help='ID of the person to retrieve locations for'
        )
        parser.add_argument(
            'verbose',
            type=int,
            default=0,
            help='to show all output'
        )

    def handle(self, *args, **options):
        """
        The function fetches and displays location data for a specified person ID within a given day,
        providing details such as time elapsed and record timestamps.

        Params:
        - person_id: int - the ID of the person to retrieve location data for
        - day: int - the number of days to go back in time
        - verbose: int - whether to show all output

        Example usage:
        - python manage.py show_last_12_h 1 0 1
        -- Fetches and displays location data for person ID 1 within the last 12 hours

        - python manage.py show_last_12_h 1 1 1
        -- Fetches and displays location data for person ID 1 within the last 24 hours

        """
        person_id = options['person_id']
        day = options['day']
        verbose = True if options['verbose'] == 1 else False

        if verbose:
            self.stdout.write(self.style.SUCCESS(
                f'Fetching location data for person ID {person_id}...'
            ))
        time_start = now()
        results = self.get_locations_for_person(person_id, day)
        time_passed = now() - time_start

        if verbose:
            self.stdout.write(
                f'Finished fetching location data for person ID {person_id} in {time_passed.total_seconds()} seconds.'
            )
        if not results:
            self.stdout.write(
                self.style.WARNING(
                    'No records found for the specified person in the last 12 hours.'
                )
            )

        first_record = results[0]
        last_record = results[-1]
        if verbose:
            self.stdout.write(f"Time between first and last record is {first_record['datetime'] - last_record['datetime'] }")
            self.stdout.write(f"First record: {first_record['datetime'].strftime('%d.%m.%Y %H:%M:%S')}")
            self.stdout.write(f"Last record: {last_record['datetime'].strftime('%d.%m.%Y %H:%M:%S')}")

        if verbose:
            self.stdout.write(f"\nAll records:")

        for result in results:
            result['datetime'] = result['datetime'].strftime('%d.%m.%Y %H:%M:%S')
            self.stdout.write(f"{result}")

    def get_locations_for_person(self, person_id: int, day: int):
        if day == 0:
            twelve_hours_ago = now() - timedelta(hours=12)
        else:
            twelve_hours_ago = now() - timedelta(days=day)

        locations = LocationRecord.objects.filter(
            people_id=person_id,
            datetime__gte=twelve_hours_ago
        ).order_by('-datetime').values(
            'id', 'latitude', 'longitude', 'datetime'
        )

        return list(locations)
