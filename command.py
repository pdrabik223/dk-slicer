# TODO: What does super() do?

class Command:

    def __init__(self) -> None:
        self.comment = "None"
        self.g_code_command = "None"
        self.parameters = []

    def gcode(self) -> str:
        return ';' + self.comment+' ; '+self.comment

    def add_offset(self, x_offset: float, y_offset: float ) -> None:
        pass

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
    
    def add_offset(self, x_offset: float, y_offset: float ) -> None:
        self.x += x_offset
        self.y += y_offset

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

from dataclasses import dataclass

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

    def add_offset(self, x_offset: float, y_offset: float )->None:
        self.p1.add_offset(x_offset,y_offset)
        self.p2.add_offset(x_offset,y_offset)  