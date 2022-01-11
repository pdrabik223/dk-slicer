# import numpy as np
# import cv2
import math
from os import curdir

# from cv2 import LSD_REFINE_ADV
from command import Command, DisEngageTool, EngageTool, Move
from gcode_file_creator import GCodeFile
# from img_reader import ImageReader


def simple_circle(center_x: float, center_y: float, radius: float):
    center_position: tuple[float, float]
    center_position = (center_x, center_y)
    alpha: float
    circle: list[Command]
    circle = []
    alpha = 10
    for angle in range(0, 361, alpha):
        circle.append(Move(x=center_x + radius * math.cos(math.radians(angle)),
                           y=center_y + radius * math.sin(math.radians(angle))))

        # r*cos(alpha) = x  r*sin(alpha) = y
        #
    return circle


def main() -> None:
    file = GCodeFile("test")

    circle = simple_circle(100, 100, 10.0)

    file.push_command(circle[0])
    file.push_command(EngageTool())

    for point in circle[1:]:
        # print(point.GCode())
        file.push_command(point)

    file.push_command(DisEngageTool())
    file.save_file()


# image = ImageReader("Lena_raw.jpg")
# image.DisplayEdges()
if __name__ == "__main__":
    main()
