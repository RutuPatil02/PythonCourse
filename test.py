def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    return (time + utc_offset)%24


print(time_from_utc(+0, 12.0))
print(time_from_utc(+1, 12.0))
print(time_from_utc(-1, 12.0))
print(time_from_utc(+6, 6.0))
# 12.0
print(time_from_utc(-7, 6.0))
# 23.0
print(time_from_utc(-1, 0.0))
  #  23.0
print(time_from_utc(-1, 23.0))
  #  22.0
print(time_from_utc(+1, 23.0))