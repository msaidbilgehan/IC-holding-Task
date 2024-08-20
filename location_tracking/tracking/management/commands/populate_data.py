from django.core.management.base import BaseCommand
from django.utils.timezone import now
import random
from datetime import timedelta
from tracking.models import LocationRecord, People


class Command(BaseCommand):
    help = 'Populate the database with dummy location data per minute'

    def add_arguments(self, parser):
        parser.add_argument(
            'is_one_by_one',
            type=int,
            default=0,
            help='Populate data one by one if 0, else bulk create'
        )
        parser.add_argument(
            'year',
            type=int,
            default=1,
            help='Number of years to generate data for'
        )

    def handle(self, *args, **options):

        self.stdout.write(
            self.style.SUCCESS(
                f'Populating location data for {options["year"]} year(s)...',
            )
        )

        if options['is_one_by_one'] == 0:
            self.stdout.write(
                self.style.SUCCESS(
                    'Populating data in bulk...',
                )
            )
            self.bulk_create(options['year'])
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    'Populating data one by one...',
                )
            )
            self.one_by_one(options['year'])

    def bulk_create(self, *args):
        year = args[0]

        # Create a dummy person
        persons = []
        persons.append(
            People.objects.get_or_create(
                first_name='Theta',
                last_name='Salsa'
            )[0]
        )
        persons.append(
            People.objects.get_or_create(
                first_name='Alfa',
                last_name='Beta'
            )[0]
        )

        # Starting point for datetime
        start_time = now()
        minute_delta = timedelta(minutes=1)

        # Generating dummy data
        counter = 0
        time_data_generation_range = 60 * 24 * 365 * year
        max_count_prediction = time_data_generation_range * len(persons)
        dummy_data = []

        time_start = now()
        for person in persons:
            for i in range(time_data_generation_range):
                dummy_data.append(
                    LocationRecord(
                        people=person,
                        datetime=start_time - minute_delta * i,
                        latitude=round(random.uniform(-90, 90), 6),
                        longitude=round(random.uniform(-180, 180), 6)
                    )
                )
                counter += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Populating (Max: {max_count_prediction}): {counter}',
                    ),
                    ending='\r'
                )
        LocationRecord.objects.bulk_create(dummy_data)
        time_passed = now() - time_start

        self.stdout.write(
            self.style.SUCCESS(
                f'First record time: {dummy_data[0].datetime}'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'Last record time: {dummy_data[-1].datetime}'
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated location data. Passed Time: {time_passed}'
            )
        )

    def one_by_one(self, *args):
        year = args[0]

        # Create a dummy person
        persons = []
        persons.append(
            People.objects.get_or_create(
                first_name='Theta',
                last_name='Salsa'
            )[0]
        )
        persons.append(
            People.objects.get_or_create(
                first_name='Alfa',
                last_name='Beta'
            )[0]
        )

        # Starting point for datetime
        start_time = now()
        minute_delta = timedelta(minutes=1)

        # Generating dummy data
        time_data_generation_range = 60 * 24 * 365 * year
        counter = 0
        max_count_prediction = time_data_generation_range * len(persons)
        time_start = now()
        for person in persons:
            for i in range(time_data_generation_range):
                LocationRecord.objects.create(
                    people=person,
                    datetime=start_time - minute_delta * i,
                    latitude=round(random.uniform(-90, 90), 6),
                    longitude=round(random.uniform(-180, 180), 6)
                )
                counter += 1
                # self.stdout.write(
                #     self.style.SUCCESS(
                #         f'Location data for "{person.first_name} {person.last_name}" at {start_time + minute_delta * i}'
                #     )
                # )
                self.stdout.write(
                        self.style.SUCCESS(
                            f'Populating (Max: {max_count_prediction}): {counter}',
                        ),
                        ending='\r'
                    )
        time_passed = now() - time_start

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated location data. Passed Time: {time_passed}'
            )
        )