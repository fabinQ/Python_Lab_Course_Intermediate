from datetime import datetime
def create_function(span):
    if span == "m": sec = 60
    if span == "h": sec = 3600
    if span == "d": sec = 86400

    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]'''.format(sec)
    exec (source, globals())
    return f

start = datetime(2023,1,1,10,0,0)
end  = datetime.now()

min = create_function("m")
print("Jest to {} minut.".format(min(start, end)))

hours = create_function("h")
print("Jest to {} godzin.".format(hours(start, end)))

days = create_function("d")
print("Jest to {} dni.".format(days(start, end)))
