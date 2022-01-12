import subprocess

def spawn_and_send_commands(pronterface_path, gcode_path):
    sub = subprocess.run([pronterface_path, "-v", "-e connect COM4" , "-e block_until_online" , f"-e load {gcode_path}", "-e print"])

if __name__ == '__main__':
    spawn_and_send_commands("C:/I/Printrun-Win-Slic3r-03Feb2015/pronsole.exe", "test.gcode")
