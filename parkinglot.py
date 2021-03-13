

class ParkingLot(object):
    """
      A singleton Class so that its variable list can be used globally and can be easily made thread safe in future

    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ParkingLot, cls).__new__(cls)
        return cls.instance
