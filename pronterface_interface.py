from operator import le
import subprocess
import sys

def spawn_and_send_commands(pronterface_path, gcode_path):
    sub = subprocess.run([pronterface_path, "-v", "-e connect COM4" , "-e block_until_online" , f"-e load {gcode_path}", "-e print", "-e exit"])

if __name__ == '__main__':
    assert len(sys.argv) > 0
    spawn_and_send_commands("C:/I/Printrun-Win-Slic3r-03Feb2015/pronsole.exe", sys.argv[1])
