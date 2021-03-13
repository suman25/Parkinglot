

class ParkingLot(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ParkingLot, cls).__new__(cls)
        return cls.instance

if __name__== '__main__':
    pass