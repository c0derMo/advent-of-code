import os
from rich.console import Console
from task import task1, task2

def parseInput(inputFilePath):
    file = open(inputFilePath)
    rawLines = file.readlines()
    file.close()
    lines = []
    for line in rawLines:
        lines.append(line.rstrip("\n"))
    return lines

if __name__ == "__main__":
    console = Console()
    inputFile = os.path.dirname(__file__) + "/input"
    lines = parseInput(inputFile)
    print("Running task 1:")
    try:
        task1(lines)
    except Exception:
        console.print_exception()
    print("Running task 2:")
    try:
        task2(lines)
    except Exception:
        console.print_exception()
