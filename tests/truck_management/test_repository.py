from django.test import TestCase
from truck_management.repository import DriverRepository
from truck_management.models import Driver, Truck
import uuid

class DriverRepositoryTestCase(TestCase):

    def setUp(self):
        self.truck1 = Truck.objects.create(number_plate="ABC123", registration_number="REG123")
        self.truck2 = Truck.objects.create(number_plate=str(uuid.uuid4())[:8], registration_number=str(uuid.uuid4())[:8])
        self.truck3 = Truck.objects.create(number_plate=str(uuid.uuid4())[:8], registration_number=str(uuid.uuid4())[:8])
        self.truck4 = Truck.objects.create(number_plate=str(uuid.uuid4())[:8], registration_number=str(uuid.uuid4())[:8])

        self.driver1 = Driver.objects.create(
            email="test1@example.com",
            name="Test Driver 1",
            mobile_number=1234567890,
            city="CityA",
            district="DistrictA",
            language="English",
            assigned_truck=self.truck1
        )
        self.driver2 = Driver.objects.create(
            email="test2@example.com",
            name="Test Driver 2",
            mobile_number=9876543210,
            city="CityB",
            district="DistrictB",
            language="Spanish"
        )

    def tearDown(self):
        Driver.objects.all().delete()
        Truck.objects.all().delete()

    def test_get_driver_by_id(self):
        driver = DriverRepository.get_driver_by_id(self.driver1.id)
        self.assertIsNotNone(driver)
        self.assertEqual(driver.email, "test1@example.com")

    def test_get_driver_by_id_not_found(self):
        driver = DriverRepository.get_driver_by_id(999)
        self.assertIsNone(driver)

    def test_get_all_drivers(self):
        drivers = DriverRepository.get_all_drivers()
        self.assertEqual(len(drivers), 2)

    def test_get_all_drivers_with_filters(self):
        filters = {'email': 'test1@example.com'}
        drivers = DriverRepository.get_all_drivers(filters)
        self.assertEqual(len(drivers), 1)
        self.assertEqual(drivers[0].email, 'test1@example.com')

    def test_create_driver(self):
        data = {
            "email": f"test3_{uuid.uuid4()}@example.com",
            "name": "Test Driver 3",
            "mobile_number": 1231231234,
            "city": "CityC",
            "district": "DistrictC",
            "language": "French",
            "assigned_truck": {
                "number_plate": str(uuid.uuid4())[:8],
                "registration_number": str(uuid.uuid4())[:8]
            }
        }
        driver_data, errors = DriverRepository.create_driver(data)
        self.assertIsNone(errors)
        self.assertIsNotNone(driver_data)
        self.assertEqual(driver_data['email'], data["email"])

    def test_create_driver_with_existing_email(self):
        data = {
            "email": "test1@example.com",
            "name": "Duplicate Test Driver",
            "mobile_number": 5555555555,
            "city": "CityD",
            "district": "DistrictD",
            "language": "German"
        }
        driver_data, errors = DriverRepository.create_driver(data)
        self.assertIsNotNone(errors)
        self.assertIn('email', errors)

    def test_create_bulk_drivers(self):
        drivers_data = [
            {
                "email": f"bulk1_{uuid.uuid4()}@example.com",
                "name": "Bulk Driver 1",
                "mobile_number": 1111111111,
                "city": "CityE",
                "district": "DistrictE",
                "language": "Italian",
                "assigned_truck": {
                    "number_plate": str(uuid.uuid4())[:8],
                    "registration_number": str(uuid.uuid4())[:8]
                }
            },
            {
                "email": f"bulk2_{uuid.uuid4()}@example.com",
                "name": "Bulk Driver 2",
                "mobile_number": 2222222222,
                "city": "CityF",
                "district": "DistrictF",
                "language": "Chinese",
                "assigned_truck": {
                    "number_plate": str(uuid.uuid4())[:8],
                    "registration_number": str(uuid.uuid4())[:8]
                }
            }
        ]
        created_drivers = DriverRepository.create_bulk_drivers(drivers_data)
        self.assertEqual(len(created_drivers), 2)
        self.assertEqual(created_drivers[0]['email'], drivers_data[0]["email"])
        self.assertEqual(created_drivers[1]['email'], drivers_data[1]["email"])
