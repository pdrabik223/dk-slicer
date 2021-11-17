from typing import Match
import numpy as np
import enum


class Command(enum, enumerate):
    Home = 1
    Move = 2
    EngageTool = 3
    DisEngageTool = 3
    Stop = 4


class IncorrectArgumentListError(Exception):
    pass


def ToGCode(command: Command, arguments: list) -> str:
    if command == Command.Home:
        if len(arguments) != 0:
            raise IncorrectArgumentListError

        return 'G28 W; Home all axis'
    if command == Command.Move:
        if len(arguments) <= 0 or len(arguments) >= 2:
            raise IncorrectArgumentListError

        return 'G0 X' + arguments[0] + "Y" + arguments[1] + "; Move "


class Syntax:
    def __init__(self, command: Command, arguments: list) -> None:
        self.command = command
        self.arguments = arguments

    def __str__(self) -> str:


class GCodeFile:
    """
    Class constructor, 
    @param filepath should be 
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

        protected: self.commad_array = []

    def AddCommand(self, command: Syntax) -> None:
        self.commad_array.append(command)

    def SaveFile(self) -> None:
        file = open(self.file_path, 'w')


print(help(GCodeFile))
