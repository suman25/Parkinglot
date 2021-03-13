import unittest
from parking_commands import *


class ParkingTest(unittest.TestCase):
    def test_create_parking_lot(self):
        result = create_parking_lot(2)
        self.assertEqual(result, 'Created parking of 2 slots')

    def test_park(self):
        result1 = assign_slot('KA-01-HH-1234', 'driver_age', '21')
        result2 = assign_slot('KA-01-HH-1233', 'driver_age', '21')
        result3 = assign_slot('KA-01-HH-1236', 'driver_age', '25')
        result4 = assign_slot('KA-02-HH-1234', '', '26')
        self.assertEqual(result1,
                         'Car with vehicle registration number "KA-01-HH-1234" has been parked at slot number 1')
        self.assertEqual(result2,
                         'Car with vehicle registration number "KA-01-HH-1233" has been parked at slot number 2')
        self.assertEqual(result3, 'Parking lot is full')
        self.assertEqual(result4, "Please add the driver's age in the command")

    def test_find_slots_for_given_driver_age(self):
        result1 = find_slots_for_given_driver_age('22')
        result2 = find_slots_for_given_driver_age('21')
        self.assertEqual(result1, '')
        self.assertEqual(result2, '1, 2')

    def test_find_slots_for_given_car_number(self):
        result1 = find_slots_for_given_car_number('KA-01-HH-1234')
        self.assertEqual(result1, 1)

    def test_find_registration_numbers_for_given_age(self):
        result1 = find_registration_numbers_for_given_age('21')
        self.assertEqual(result1, ['KA-01-HH-1234', 'KA-01-HH-1233'])

    def test_deassign(self):
        result1 = de_assign_slot(1)
        self.assertEqual(result1,
                         'slot number 1 vacated, the car with vehicle registration number "KA-01-HH-1234" left the '
                         'space , the driver of the ''car was of age 21')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ParkingTest('test_create_parking_lot'))
    suite.addTest(ParkingTest('test_park'))
    suite.addTest(ParkingTest('test_find_slots_for_given_driver_age'))
    suite.addTest(ParkingTest('test_find_slots_for_given_car_number'))
    suite.addTest(ParkingTest('test_find_registration_numbers_for_given_age'))
    return suite


mySuit = suite()
runner = unittest.TextTestRunner(failfast=True)
runner.run(mySuit)
