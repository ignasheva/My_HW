def check_power_of_2(a: int) -> bool:
    return a and (not (a & (a - 1)))
