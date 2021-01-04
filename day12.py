import re
import turtle
from typing import List, Tuple


def get_input(path: str):
    pattern = re.compile('([A-Z])([0-9]+)')
    input = []
    with open(path, 'r') as f:
        for line in f.readlines():
            groups = pattern.fullmatch(line.strip()).groups()
            input.append((groups[0], int(groups[1])))
    return input


class Ferry:

    def __init__(self, instructions: List[Tuple[str, int]]):
        self.screen = turtle.getscreen()
        # self.screen.setup(2000, 2000)
        self.screen.tracer(False)
        self.turtle = turtle.Turtle()
        self.wrc = [10, 1]  # waypoint realtive coordinates
        self.instructions = instructions

    def execute_instructions(self, waypoint: bool = False):
        if not waypoint:
            for instruction in self.instructions:
                self.move(instruction[0], instruction[1])
        else:
            for instruction in self.instructions:
                self.move_with_waypoint(instruction[0], instruction[1])

    def move(self, step: str, value: int) -> None:
        if step == 'N':
            self.turtle.goto(self.turtle.pos() + (0, value))
        elif step == 'S':
            self.turtle.goto(self.turtle.pos() + (0, -value))
        elif step == 'E':
            self.turtle.goto(self.turtle.pos() + (value, 0))
        elif step == 'W':
            self.turtle.goto(self.turtle.pos() + (-value, 0))
        elif step == 'L':
            self.turtle.left(value)
        elif step == 'R':
            self.turtle.right(value)
        elif step == 'F':
            self.turtle.forward(value)
        return None

    def move_with_waypoint(self, step: str, value: int) -> None:
        if step == 'N':
            self.wrc[1] += value
        elif step == 'S':
            self.wrc[1] -= value
        elif step == 'E':
            self.wrc[0] += value
        elif step == 'W':
            self.wrc[0] -= value
        elif step == 'L' or step == 'R':
            self.rotate_waypoint(step, value)
        elif step == 'F':
            self.turtle.goto(self.turtle.pos() + (self.wrc[0] * value, self.wrc[1] * value))
        return None

    def rotate_waypoint(self, step: str, value: int) -> None:
        if (step == 'R' and value == 90) or (step == 'L' and value == 270):
            self.wrc[0], self.wrc[1] = self.wrc[1], -self.wrc[0]
        elif (step == 'R' and value == 270) or (step == 'L' and value == 90):
            self.wrc[0], self.wrc[1] = -self.wrc[1], self.wrc[0]
        elif value == 180:
            self.wrc[0], self.wrc[1] = -self.wrc[0], -self.wrc[1]
        return None

    def get_position(self) -> Tuple[float, float]:
        return self.turtle.pos()

    def reset_position(self) -> None:
        self.turtle.home()
        return None


if __name__ == '__main__':
    input = get_input('input/day12.txt')

    ferry = Ferry(input)
    ferry.execute_instructions()
    final_position = ferry.get_position()
    print(final_position)
    print(f'Manhattan distance: {int(abs(final_position[0]) + abs(final_position[1]))}')

    ferry.reset_position()
    ferry.execute_instructions(waypoint=True)
    final_position_with_waypoint = ferry.get_position()
    print(final_position_with_waypoint)
    print(
        f'Manhattan distance (waypoint): {abs(final_position_with_waypoint[0]) + abs(final_position_with_waypoint[1])}')
