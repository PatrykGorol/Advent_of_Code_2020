from typing import List, Union


def get_input(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()
        my_time = int(lines[0].strip())
        bus_schedule = [int(num) if num != 'x' else 'x' for num in lines[1].strip().split(',')]
        return my_time, bus_schedule


def find_next_bus(my_time: int, bus_schedule: List[Union[int, str]]):
    next_departures = list_next_departures(my_time, bus_schedule)
    earliest_departure = min(next_departures.values())
    for bus in next_departures:
        if next_departures[bus] == earliest_departure:
            return bus, earliest_departure


def list_next_departures(my_time: int, bus_schedule: List[Union[int, str]]):
    next_departures = {}
    for bus in bus_schedule:
        if bus != 'x':
            if my_time % bus == 0:
                next_departures[bus] = my_time
            else:
                next_departures[bus] = (my_time // bus + 1) * bus
    return next_departures


def find_timestamp_matching_schedule(bus_schedule: List[Union[int, str]]) -> int:
    # based on Seoane8 solution from:
    # https://dev.to/rpalo/advent-of-code-2020-solution-megathread-day-13-shuttle-search-313f

    modulos = {bus: -i % bus for i, bus in enumerate(bus_schedule) if bus != 'x'}
    timestamp = 0
    increment = 1
    for bus in modulos.keys():
        while timestamp % bus != modulos[bus]:
            timestamp += increment
        increment *= bus
    return timestamp


# def find_timestamps_matching_schedule(bus_schedule: List[Union[int, str]]): # not effective, takes to much time
#     max_index, max_num = find_max(bus_schedule)
#     busses = [i for i in enumerate(bus_schedule) if i[1] != 'x']
#     my_num = 0
#     my_num += max_num
#     timestamps = [my_num + (i - max_index) for i, num in busses]
#     while not check_constraints(timestamps, busses):
#         my_num += max_num
#         # print('-------------------------')
#         print(my_num)
#         timestamps = [my_num + (i - max_index) for i, num in busses]
#     return timestamps
#
#
# def find_max(bus_schedule: List[Union[int, str]]):
#     max_num = max(num for num in bus_schedule if num != 'x')
#     return bus_schedule.index(max_num), max_num
#
#
# def check_constraints(timestamps: List[int], busses):
#     for i in range(len(timestamps)):
#         if timestamps[i] % busses[i][1] != 0:
#             return False
#     return True


if __name__ == '__main__':
    my_time, bus_schedule = get_input('input/day13.txt')
    # bus_schedule = [17, 'x', 13, 19]
    # bus_schedule = [67, 7, 59, 61]
    # bus_schedule = [67, 'x', 7, 59, 61]
    # bus_schedule = [67, 7, 'x', 59, 61]
    # bus_schedule = [1789, 37, 47, 1889]
    # print(bus_schedule)
    bus, next_departure = find_next_bus(my_time, bus_schedule)
    print(f'Next bus: {bus}, at {next_departure} (in {next_departure - my_time} minutes).')
    print(f'Bus ID multiplied by number of minutes: {bus * (next_departure - my_time)}')
    timestamps = find_timestamp_matching_schedule(bus_schedule)
    print(f'Timestamp matching schedule: {timestamps}')
