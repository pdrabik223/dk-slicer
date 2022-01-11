from types import coroutine
from typing import Match, NoReturn
import numpy as np
import enum
from typing import List
from command import *


class IncorrectArgumentListError(Exception):
    pass


class GCodeFile:
    """
    Class constructor,
    @param filepath should be
    """

    def __init__(self, file_path: str) -> None:
        # checking if ".gcode" statement is present at the end of the file
        if file_path[len(file_path) - 6:len(file_path)] != '.gcode':
            file_path += '.gcode'

        self.file_path = file_path

        self._commad_array: List[str]
        self._commad_array = []

    def StartUp(self) -> List[str]:
        startup_commands: List[str]
        startup_commands = []
        startup_commands.append("M115 U3.8.1 ; tell printer latest fw version")
        startup_commands.append("M862.3 P \"MK3S\" ; printer model check")
        startup_commands.append("M862.1 P0.4 ; nozzle diameter check")
        startup_commands.append("M104 S20 ; set extruder temp")
        startup_commands.append("M140 S20 ; set bed temp")
        startup_commands.append("M107 ; turn off fan")
        startup_commands.append(
            "M201 X1000 Y1000 Z200 ; sets maximum accelerations, mm/sec^2")
        startup_commands.append(
            "M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm/sec")
        startup_commands.append(
            "M204 P1250 R1250 T1250 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2")
        startup_commands.append(
            "M205 X8.00 Y8.00 Z0.40 E4.50 ; sets the jerk limits, mm/sec")
        startup_commands.append(
            "M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec")
        startup_commands.append("G1 F200.000; set movement speed")
        startup_commands.append("M73 P0 R30; set current progress")
        startup_commands.append("M73 Q0 S30; set current progress")
        startup_commands.append("G90 ; use absolute coordinates")
        startup_commands.append("G21 ; set units to millimeters")
        startup_commands.append(
            "M221 S0; set extrude factor override percentage")
        startup_commands.append("M83 ; extruder relative mode")
        startup_commands.append(DisEngageTool().GCode())
        startup_commands.append(Home().GCode())
        startup_commands.append("G80 ; mesh bed leveling")

        startup_commands.append("; End of startup")

        startup_commands = ["\n" + command for command in startup_commands]

        return startup_commands

    def ShutDown(self) -> List[str]:
        shutdown_commads: List[str]
        shutdown_commads = []
        shutdown_commads.append(DisEngageTool().GCode())
        shutdown_commads.append("M73 P100 R0; set current progress")
        shutdown_commads.append("M73 Q100 S0; set current progress")
        shutdown_commads.append("G1 Z10 ; Move print head up")
        shutdown_commads.append("G1 X0 Y200 F3000 ; home X axis")
        shutdown_commads.append("M84 ; disable motors")

        shutdown_commads = ["\n" + command for command in shutdown_commads]

        return shutdown_commads

    def PushCommand(self, command: Command) -> None:
        self._commad_array.append("\n" + command.GCode())

    def SaveFile(self) -> None:

        with open(self.file_path, 'w') as file:
            file.writelines(
                [";G-Code generated automatically using drab0l1-slicer"])
            file.writelines(self.StartUp())
            file.writelines(self._commad_array)
            file.writelines(self.ShutDown())
