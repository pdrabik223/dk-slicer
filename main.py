# import numpy as np
# import cv2
import math
from os import curdir
import numpy as np
import math

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


def test_print():
    
    file = GCodeFile("test")

    space = np.linspace(10, 100, 500)
    sinusoid = np.sin(space) + 50
    
    file.push_command(Move(space[0],sinusoid[0]))
    file.push_command(EngageTool())
    for x, y in zip(space, sinusoid):
        file.push_command(Move(x,y))
    file.push_command(DisEngageTool())
 
    circle = simple_circle(150, 150, 40)
    file.push_command(circle[0])
    file.push_command(EngageTool())
    for point in circle[1:]:
        # print(point.GCode())
        file.push_command(point)
    file.push_command(DisEngageTool())

    circle = simple_circle(140, 40, 40)
    file.push_command(circle[0])
    file.push_command(EngageTool())
    circle_random = circle[1:].copy()
    np.random.shuffle(circle_random)
    for point in circle_random:
        # print(point.GCode())
        file.push_command(point)
    file.push_command(DisEngageTool())
           
    space = np.linspace(10, 100, 500)
    sinusoid_higher_freq = [150 + math.sin(4 * x) for x in space]

    file.push_command(Move(space[0],sinusoid_higher_freq[0]))
    file.push_command(EngageTool())
    for x, y in zip(space, sinusoid_higher_freq):
        file.push_command(Move(y,x))
    file.push_command(DisEngageTool())
    
    
        
    file.save_file()



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
    # main()
    test_print()
