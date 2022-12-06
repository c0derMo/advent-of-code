import subprocess
import time

def runDay(day, console):
    runTask(day, 1, console)
    runTask(day, 2, console)

def testDay(day, console):
    runTask(day, 1, console, True)
    runTask(day, 2, console, True)

def runTask(day, task, console, test=False):
    console.rule(f"[yellow]Task {task}")
    startTime = time.time()
    cmd = ["python", "-u", f"./src/day{str(day).rjust(2, '0')}/runner.py", str(task)]
    if test:
        cmd.append("test")
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    buf = b""
    while p.poll() is None:
        out = p.stdout.read(1)
        if out != b'':
            if out == b'\n':
                console.log(buf.decode("utf8"))
                buf = b""
            else:
                buf += out
    out = p.stdout.read()
    if out != b'':
        buf += out
        console.log(buf.decode("utf8"))
    endTime = time.time()
    timeDiff = round(endTime - startTime, 3)
    if p.returncode == 0:
        console.log(f"[green]Task {task} finished execution successfully in {timeDiff}s.")
    else:
        console.log(f"[bold red]Task {task} failed execution in {timeDiff}s!")