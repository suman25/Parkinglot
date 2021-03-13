from parking_decorators import ParkingApp
from parkinglot import ParkingLot

app = ParkingApp()
parking_lot = ParkingLot()


class Customer(object):
    def __init__(self, car_registration_number, age):
        self.car_registration_number = car_registration_number
        self.age = age


@app.parking_functions('Create_parking_lot $length')
def create_parking_lot(length):
    parking_lot = ParkingLot()
    parking_lot.parking_slots = [None] * int(length)
    return 'Created parking of {} slots'.format(length)


@app.parking_functions('Park $car_registration_number $driver_age $age')
def assign_slot(car_registration_number_number, driver_age, age):
    slot_to_be_assigned = next(
        slot for slot in range(len(parking_lot.parking_slots)) if parking_lot.parking_slots[slot] is None)
    if slot_to_be_assigned is not None and driver_age:
        customer = Customer(car_registration_number_number, int(age))
        parking_lot.parking_slots.insert(slot_to_be_assigned, customer)
        return 'Car with vehicle registration number "{}" has been parked at slot number {}'.format(
            customer.car_registration_number, slot_to_be_assigned+1)
    else:
        return 'Parking lot is full'


@app.parking_functions('Slot_numbers_for_driver_of_age $age')
def find_slots_for_given_driver_age(age):
    slots_for_certain_age = [slot+1 for slot, customer in enumerate(parking_lot.parking_slots) if
                              customer and customer.age == int(age)]
    return slots_for_certain_age


@app.parking_functions('Slot_number_for_car_with_number $ car_registration_number')
def find_slots_for_given_number(car_registration_number_number):
    slot_for_certain_car_number = next(
        slot+1 for slot, customer in enumerate(parking_lot.parking_slots) if
        customer.car_registration_number == car_registration_number_number)
    return slot_for_certain_car_number


@app.parking_functions('Leave $slot')
def de_assign_slot(slot_number):
    int_slot_number = int(slot_number)- 1
    slot_to_be_removed = parking_lot.parking_slots[int_slot_number]
    parking_lot.parking_slots[int_slot_number] = None
    return 'slot number {} vacated, the car with vehicle registration number "{}" left the space , the driver of the ' \
           'car was of age {}' \
        .format(slot_number, slot_to_be_removed.car_registration_number, slot_to_be_removed.age)


@app.parking_functions('Vehicle_registration_number_for_driver_of_age $age')
def find_registration_numbers_for_given_age(age):
    registration_numbers = [customer.car_registration_number for customer in parking_lot.parking_slots if customer and
                            customer.age == int(age)]
    return registration_numbers


if __name__ == '__main__':
    app.run()
