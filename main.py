# import numpy as np
# import cv2
from command import Command, DisEngageTool, EngageTool, Move
from gcode_file_creator import GCodeFile


def Circle(center_x: float, center_y: float, radius: float) -> list[Command]:

    center_position: tuple(float, float)
    center_position = (center_x, center_y)
    x = radius
    y = 0
    err = 0
    circle: list[Command]
    circle = []
    while x >= y:
        circle.append(
            Move(x=center_position[0] + x, y=center_position[1] + y))
        circle.append(
            Move(x=center_position[1] + y, y=center_position[0] + x))
        circle.append(
            Move(x=center_position[1] + x, y=center_position[0] + y))
        circle.append(
            Move(x=center_position[1] + x, y=center_position[0] - y))
        circle.append(
            Move(x=center_position[1] + y, y=center_position[0] - x))
        circle.append(
            Move(x=center_position[1] - y, y=center_position[0] - x))
        circle.append(
            Move(x=center_position[1] - x, y=center_position[0] - y))
        circle.append(
            Move(x=center_position[1] - x, y=center_position[0] + y))
        circle.append(
            Move(x=center_position[1] - y, y=center_position[0] + x))

        if err <= 0:
            y += 1
            err += 2 * y + 1
        else:
            x -= 1
            err -= 2 * x + 1
    return circle


file = GCodeFile("test")


circle = Circle(50, 50, 10.0)

file.PushCommand(circle[0])
file.PushCommand(EngageTool())

for point in circle[1:]:
    # print(point.GCode())
    file.PushCommand(point)


file.PushCommand(DisEngageTool())
file.SaveFile()
