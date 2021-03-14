from parking_decorators import ParkingApp
from parkinglot import ParkingLot
import re

app = ParkingApp()
parking_lot = ParkingLot()


class Customer(object):
    def __init__(self, car_registration_number, age):
        self.car_registration_number = car_registration_number
        self.age = age


@app.parking_functions('Create_parking_lot $length')
def create_parking_lot(length):
    """
    create a parking_slot list with the length sent in params
    :param length:string
    :return: string
     """
    parking_lot.parking_slots = [None] * (int(length))
    return 'Created parking of {} slots'.format(length)


@app.parking_functions('Park $car_registration_number $driver_age $age')
def assign_slot(*args):
    """
    this function gets *args so that changes for more args can be done easily, first check if the arguments are valid
    , get the first None element in the list , insert a object with values in list :param args: multiple arguments
    :return:
    """
    try:
        is_valid, message = check_for_valid_args(*args)
        if not is_valid:
            return message
        slot_to_be_assigned = next(
            (slot for slot in range(len(parking_lot.parking_slots)) if parking_lot.parking_slots[slot] is None), None)
        if slot_to_be_assigned is not None:
            customer = Customer(args[0], int(args[2]))
            parking_lot.parking_slots[slot_to_be_assigned] = customer
            return 'Car with vehicle registration number "{}" has been parked at slot number {}'.format(
                customer.car_registration_number, slot_to_be_assigned + 1)
        else:
            return 'Parking lot is full'
    except AttributeError:
        return 'Please create a parking lot first'
    except BaseException as e:
        return e


def check_for_valid_args(*args):
    try:
        plate_format = re.compile('^[a-zA-Z]{2}-[0-9]{2}-[a-zA-z]{2}-[0-9]{4}$')
        car_registration_number = args[0]
        if plate_format.match(car_registration_number) is None:
            return False, 'Invalid registration Plate'
        if not args[2].isdigit():
            return False, 'Age must be a number'

        if args[1] != 'driver_age':
            return False, "Please add the driver's age in the command"

        return True, "Valid Arguments"
    except IndexError:
        return False, 'Arguments Missing'


@app.parking_functions('Slot_numbers_for_driver_of_age $age')
def find_slots_for_given_driver_age(age):
    slots_for_certain_age = [slot + 1 for slot, customer in enumerate(parking_lot.parking_slots) if
                             customer and customer.age == int(age)]
    return str(slots_for_certain_age)[1:-1] if slots_for_certain_age else None


@app.parking_functions('Slot_number_for_car_with_number $ car_registration_number')
def find_slots_for_given_car_number(car_registration_number_number):
    slot_for_certain_car_number = next((
        slot + 1 for slot, customer in enumerate(parking_lot.parking_slots) if
        customer.car_registration_number == car_registration_number_number), None)
    return slot_for_certain_car_number


@app.parking_functions('Leave $slot')
def de_assign_slot(slot_number):
    """
    set the value none at the position sent in param
    :param slot_number:str
    :return: str
    """
    int_slot_number = int(slot_number) - 1
    slot_to_be_removed = parking_lot.parking_slots[int_slot_number]
    parking_lot.parking_slots[int_slot_number] = None
    return 'slot number {} vacated, the car with vehicle registration number "{}" left the space , the driver of the ' \
           'car was of age {}' \
        .format(slot_number, slot_to_be_removed.car_registration_number, slot_to_be_removed.age)


@app.parking_functions('Vehicle_registration_number_for_driver_of_age $age')
def find_registration_numbers_for_given_age(age):
    try:
        registration_numbers = [customer.car_registration_number for customer in parking_lot.parking_slots if
                                customer and
                                customer.age == int(age)]
        return str(registration_numbers)[1:-1] if registration_numbers else None
    except ValueError:
        return 'Age should be a number'


if __name__ == '__main__':
    app.run()
