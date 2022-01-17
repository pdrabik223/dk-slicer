# TODO: What does super() do?

from dataclasses import dataclass
from turtle import width
from distutils import command


class Command:

    def __init__(self) -> None:
        self.comment = "None"
        self.g_code_command = "None"
        self.parameters = []

    def gcode(self) -> str:
        return ';' + self.comment+' ; '+self.comment

    def add_offset(self, x_offset: float, y_offset: float) -> None:
        pass

    def fits_in_boundaries(self, x_range, y_range) -> bool:
        return True


class Home(Command):
    def __init__(self) -> None:
        # super().__init__()
        self.comment = "Home all axis"
        self.g_code_command = "G28 W"

    def gcode(self) -> str:
        return self.g_code_command + ' ; ' + self.comment


class Move(Command):
    """
    x position to move to on x axis
    y position to move to on y axis
    z position to move to on z axis

    f feed rate, how fast should move to that place [millimiters / minute]
    """

    def __init__(self, x: float, y: float) -> None:
        # super().__init__()
        self.g_code_command = 'G1'
        self.x = x
        self.y = y
        self.f = None

    def gcode(self) -> str:
        output = self.g_code_command
        if self.x != None:
            output = output + ' X' + str(round(self.x, 3))
        if self.y != None:
            output = output + ' Y' + str(round(self.y, 3))
        if self.f != None:
            output = output + ' F' + str(round(self.f, 6))
            # out += f"x={self.f:.2f}"
        output += ' E0.01'
        return output

    def add_offset(self, x_offset: float, y_offset: float) -> None:
        self.x += x_offset
        self.y += y_offset

    def fits_in_boundaries(self, x_range, y_range) -> bool:
        if self.x < x_range[0] or self.x > x_range[1]:
            return False
        if self.y < y_range[0] or self.y > y_range[1]:
            return False

        return True


class EngageTool(Command):
    """
    moves tool downwards, to on position 
    """

    def __init__(self) -> None:
        # super().__init__()
        self.comment = "Engage tool"
        self.g_code_command = "G1"
        self.z = 0.4  # 5 millmiters above bed is on position

    def gcode(self) -> str:
        return self.g_code_command + ' Z'+str(self.z)+' ; '+self.comment


class DisEngageTool(Command):
    """
    moves tool upwards, to off position 
    """

    def __init__(self) -> None:
        # super().__init__()
        self.comment = "Disengage tool"
        self.g_code_command = "G1"
        self.z = 1  # 10 millmiters above bed is on position

    def gcode(self) -> str:
        return self.g_code_command + ' Z' + str(self.z) + ' ; '+self.comment


class Wait(Command):
    """
    waits for specified time 
    time is passed as milliseconds
    if no time walu will be specified printer wil wait for second 
    """

    def __init__(self, time: int) -> None:
        # super().__init__()
        self.comment = "Wait"
        self.g_code_command = "G4"
        self.time = time

    def gcode(self) -> str:
        return self.g_code_command + ' P' + self.time + ' ; ' + self.comment


@dataclass
class Vec2:
    x: float
    y: float


class DrawLine(Command):
    """
    Engages the tool draws the line from p1 to p2
    than disengages the tool
    """

    def __init__(self, p1: Vec2, p2: Vec2, engage=True, disengage=True):
        # super().__init__()
        self.p1 = p1
        self.p2 = p2

        self.engage = engage
        self.disengage = disengage

    def gcode(self):
        commands = []

        commands.append(Move(x=self.p1.x, y=self.p1.y).gcode())

        if self.engage:
            commands.append(EngageTool().gcode())

        commands.append(Move(x=self.p2.x, y=self.p2.y).gcode())

        if self.disengage:
            commands.append(DisEngageTool().gcode())

        return "\n".join(commands)

    def add_offset(self, x_offset: float, y_offset: float) -> None:
        self.p1.x += x_offset
        self.p1.y += y_offset
        self.p2.x += x_offset
        self.p2.y += y_offset

    def fits_in_boundaries(self, x_range, y_range) -> bool:
        if self.p1.x < x_range[0] or self.p1.x > x_range[1]:
            return False
        if self.p2.x < x_range[0] or self.p2.x > x_range[1]:
            return False
        if self.p1.y < y_range[0] or self.p1.y > y_range[1]:
            return False
        if self.p2.y < y_range[0] or self.p2.y > y_range[1]:
            return False

        return True

# class DrawSquare(Command):
#     def __init__(self, x:float,y:float,width:float,height:float) -> None:
#        self.x = x
#        self.y = y
#        self.width = width # change beetwen corners on x axis
#        self.height = height # change beetwen corners on y axis
#     def gcode(self):
#         commands = []
#         commands.append(DisEngageTool())
#         commands.append(Move(self.x,self.y))
#         commands.append(EngageTool())
#         commands.append(Move(self.x+width))
