from django.core.management.base import BaseCommand
from django.utils.timezone import now
from tracking.models import LocationRecord
from datetime import timedelta


class Command(BaseCommand):
    help = 'Display the latest location data for a specific person'

    def add_arguments(self, parser):
        # Adding a command line option to specify the person's ID
        parser.add_argument(
            'person_id', type=int, help='ID of the person to retrieve the latest location for'
        )

    def handle(self, *args, **options):
        person_id = options['person_id']
        self.stdout.write(
            self.style.SUCCESS(
                f'Fetching the latest location data for person ID {person_id}...'
            )
        )
        result = self.get_latest_location_for_person(person_id)
        if result:
            self.stdout.write(f"{result}")
        else:
            self.stdout.write(self.style.WARNING(
                'No records found for the specified person.'
            ))

    def get_latest_location_for_person(self, person_id):
        try:
            latest_location = LocationRecord.objects.filter(
                people_id=person_id,
            ).latest('datetime')

            first_location = LocationRecord.objects.filter(
                people_id=person_id,
            ).order_by('datetime').first()  # Orders by datetime ascending

            if not first_location:
                return None

            self.stdout.write(
                self.style.SUCCESS(
                    f'First location record for person ID {person_id} found at {first_location.datetime} (ID: {first_location.id})'  # type: ignore
                )
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Latest location record for person ID {person_id} found at {latest_location.datetime} (ID: {latest_location.id})'  # type: ignore
                )
            )


            return {
                "first_record": {
                    "id": first_location.id,  # type: ignore
                    "latitude": first_location.latitude,
                    "longitude": first_location.longitude,
                    "datetime": first_location.datetime.strftime('%d.%m.%Y %H:%M:%S')
                },
                "latest_record": {
                    "id": latest_location.id,  # type: ignore
                    "latitude": latest_location.latitude,
                    "longitude": latest_location.longitude,
                    "datetime": latest_location.datetime.strftime('%d.%m.%Y %H:%M:%S')
                }
            }
        except LocationRecord.DoesNotExist:
            return None
