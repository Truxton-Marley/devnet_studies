import datetime

dir(datetime)
#Five major modules: date, time, datetime, timedelta, timezone
#Less common: tzinfo

datetime.datetime.now()  ## Return the current time (year, month, day, hour, minute, sec, microseconds)

start = datetime.datetime.now()

start.replace(hour=13, minute=0)

datetime.datetime.now() - start  # Returns a timedelta

one_hour = datetime.timedelta(hours=5)

two_days = datetime.timedelta(days=3)

future = start + one_hour
past = start - two_days

past.date()
future.time()

##########        Code Challenge        ############

## Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime

import datetime

def to_string(dt_obj):
    return dt_obj.strftime("%d %B %Y")

def from_string(date_string, strftime_string):
    return datetime.datetime.strptime(date_string, strftime_string)




