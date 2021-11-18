

class Command:

    def __init__(self) -> None:
        self.comment = "None"
        self.g_code_command = "None"
        self.parameters = []

    def GCode(self) -> str:
        return ';' + self.comment+' ; '+self.comment


class Home(Command):
    def __init__(self) -> None:
        super().__init__()
        self.comment = "Home all axis"
        self.g_code_command = "G28 W"

    def GCode(self) -> str:
        return self.g_code_command + ' ; ' + self.comment


class Move(Command):
    """
    x position to move to on x axis
    y position to move to on y axis
    z position to move to on z axis

    f feed rate, how fast should move to that place [millimiters / minute]
    """

    def __init__(self, x: float, y: float, f: int) -> None:
        super().__init__()
        self.g_code_command = 'G1'
        self.x = x
        self.y = y
        self.f = f

    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.g_code_command = 'G1'
        self.x = x
        self.y = y
        self.f = None

    def GCode(self) -> str:
        output = self.g_code_command
        if self.x != None:
            output = output + ' X' + str(self.x)
        if self.y != None:
            output = output + ' Y' + str(self.y)
        if self.f != None:
            output = output + ' F' + str(self.f)
        output += ' E0.01'
        return output


class EngageTool(Command):
    """
    moves tool downwards, to on position 
    """

    def __init__(self) -> None:
        super().__init__()
        self.comment = "Engage tool"
        self.g_code_command = "G1"
        self.z = 5.0  # 5 millmiters above bed is on position

    def GCode(self) -> str:
        return self.g_code_command + ' Z'+str(self.z)+' ; '+self.comment


class DisEngageTool(Command):
    """
    moves tool upwards, to off position 
    """

    def __init__(self) -> None:
        super().__init__()
        self.comment = "Disengage tool"
        self.g_code_command = "G1"
        self.z = 10.0  # 10 millmiters above bed is on position

    def GCode(self) -> str:
        return self.g_code_command + ' Z' + str(self.z) + ' ; '+self.comment


class Wait(Command):
    """
    waits for specified time 
    time is passed as milliseconds
    if no time walu will be specified printer wil wait for second 
    """

    def __init__(self, time: int) -> None:
        super().__init__()
        self.comment = "Wait"
        self.g_code_command = "G4"
        self.time = time

    def __init__(self) -> None:
        super().__init__()
        self.comment = "Wait"
        self.g_code_command = "G4"
        self.time = 1000

    def GCode(self) -> str:
        return self.g_code_command + ' P' + self.time + ' ; ' + self.comment
