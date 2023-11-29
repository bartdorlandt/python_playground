
# divmod builtin function.
# inputs 2 x int, returns the amount of divisions and the remainder
# Perfect for time calculations

def get_hour_min_sec(seconds: int) -> tuple[int, int,int]:
    """get_hour_min_sec."""
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, sec
