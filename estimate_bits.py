from math import log, ceil, floor


def round_power2(num):
    res = floor(log(num, 2)), ceil(log(num, 2))
    return min(res, key=lambda x: abs(num - 2 ** x))

# Num cpu cores and clock speed in GHz
def print_work_bits(cores, speed):
    numBillions = cores * speed
    numBits = round_power2(numBillions) + 30  # 10 ^ 9 = 2 ^ 30
    dayBits = numBits + 17  # 2 ^ 17 seconds in a day
    dayBits_for_128 = 128 - dayBits
    yearBits_for_128 = dayBits_for_128 - 8  # divide by (2 ^ 8 days in a year)

    print(f"Bits of work per 24 hrs: {dayBits}")
    print(f"Days for 128 bits of work: {dayBits_for_128}")
    print(f"Years for 128 bits of work: {yearBits_for_128}")


attackers = {
	"person description": (1, 2),  # give tuple with (number_of_cores, clock_speed_Ghz)
	"person description 2": (4, 2),  # give tuple with (number_of_cores, clock_speed_Ghz)
	"person description 3": (1000, 100000000),  # give tuple with (number_of_cores, clock_speed_Ghz)
}

for key in attackers:
    print(f"{key} at {attackers[key][1]} Ghz")
    print_work_bits(*attackers[key])


