from django.core.management.base import BaseCommand
from django.utils.timezone import now
import random
from datetime import timedelta
from tracking.models import LocationRecord, People


class Command(BaseCommand):
    help = 'Populate the database with dummy location data per minute'

    def add_arguments(self, parser):
        parser.add_argument(
            'number_of_person',
            type=int,
            default=1,
            help='Number of people to generate data for'
        )
        parser.add_argument(
            'number_of_years',
            type=int,
            default=1,
            help='Number of years to generate data for'
        )

    def handle(self, *args, **options):

        self.stdout.write(
            self.style.SUCCESS(
                f'Populating dummy {options["number_of_person"]} person and location data for {options["number_of_years"]} year(s) per person...',
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Populating data in bulk...',
            )
        )
        self.bulk_create(
            number_of_person=options['number_of_person'],
            number_of_years=options['number_of_years']
        )

    def bulk_create(self, number_of_person, number_of_years):
        """
        The function generates dummy location data for a specified number of people over a given number of years.
        """

        # Create a dummy person
        persons = []
        for i in range(number_of_person):
            persons.append(
                People.objects.get_or_create(
                    first_name=f'Alfa{i}',
                    last_name=f'Theta{i}'
                )[0]
            )

        # Starting point for datetime
        start_time = now()
        minute_delta = timedelta(minutes=1)

        # Generating dummy data
        counter = 0
        time_data_generation_range = 60 * 24 * 365 * number_of_years
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
