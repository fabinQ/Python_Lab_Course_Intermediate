import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException("NameError: ")
        if self.start > self.end:
            raise TripDateException("DateError: ")

    @classmethod
    def publish_offer(cls, trips):

        list_of_errors = []

        for trip in trips:
            try:
                trip.check_data()
            except TripNameException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except TripDateException as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))

        if len(list_of_errors) > 0:
            raise Exception("The list of trips has errors: {}".format(list_of_errors))
        else:
            print('the offer will be published...')

class TripException (Exception):

    def __init__(self, text, discripton):
        super().__init__(text)
        self.disctription = discripton

    def __str__(self):
        return "Trip exception - {} {}".format(super().__str__(), self.disctription)

class TripNameException(TripException):
    def __init__(self,text):
        super().__init__(text, 'Name of the trip is missing. You need to name the trip somehow...')


class TripDateException(TripException):
    def __init__(self, text):
        super().__init__(text, 'The dates are incorrect. The starting date should be earlier than the ending date...')



trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('SP-WAW', '', dt.date(2023, 6, 12), dt.date(2023, 6, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')
