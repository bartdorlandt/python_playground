
# divmod builtin function.
# inputs 2 x int, returns the amount of divisions and the remainder
# Perfect for time calculations

def get_hour_min_sec(seconds: int) -> tuple[int, int,int]:
    """get_hour_min_sec."""
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, sec


def get_days_hour_min_sec(seconds: int) -> tuple[int, int, int,int]:
    """get_days_hour_min_sec."""
    hours, minutes, sec = get_hour_min_sec(seconds)
    days, hours = divmod(hours, 24)
    return days, hours, minutes, seconds


assert get_hour_min_sec(460002) == (127, 46, 42)
assert get_hour_min_sec(3600) == (1, 0, 0)
assert get_days_hour_min_sec(460002) == (5, 7, 46, 460002)
