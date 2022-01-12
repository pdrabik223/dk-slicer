import subprocess


def spawn_and_send_commands(pronterface_path, commands):
    with subprocess.Popen([pronterface_path],
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE) as proc:
        for command in commands:
            while not proc.stdin.writable():
                print(proc.stdout.readlines())
            
            proc.stdin.writelines([command])
