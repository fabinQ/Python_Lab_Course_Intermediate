import datetime as dt


class Trip:
    # trips = []
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
        # Trip.trips.append(self)
        # print(Trip.trips)
    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")
    @classmethod
    def publish_offer(cls, trips):
        # print(cls.trips)
        # print(trips)
        list_of_errors = []
        for trip in trips:
            try:
                # cls.check_data(trip)
                trip.check_data()
            except ValueError as e:
                list_of_errors.append("{}:{}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}:{}".format(trip.symbol, str(e)))
        if not len(list_of_errors) == 0:
            # raise Exception(The list of trips has errors:", list_of_errors)
            raise Exception("The list of trips has errors: {}".format(list_of_errors))
        else:
            print("The offer will be published...")

trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12)),
    Trip('IT-WAW', '', dt.date(2023, 6, 21), dt.date(2023, 6, 20))
]
# for trip in trips:
#     trip
try:
    print("Checing trips compatibility...")
    # 1/0
    Trip.publish_offer(trips)
    print('Done')
except Exception as e:
    print("FATAL ERORRRRRR !!!!!!111")
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')