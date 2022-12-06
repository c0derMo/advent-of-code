import sys
from datetime import date
from rich.progress import Progress
from rich import print
from rich.console import Console
from runner import runDay, testDay
from initDay import getInput, makeNewDay

def getDay():
    day = -1
    if len(sys.argv) >= 3:
        try:
            day = int(sys.argv[2])
        except:
            pass
    else:
        day = date.today().day
    if day <= 0 or day >= 25:
        console.log("[red]Invalid day. Should be 1-25, was " + str(day))
        exit(1)
    return day

if __name__ == '__main__':
    console = Console()
    if len(sys.argv) <= 1 or sys.argv[1] == "help":
        console.print("Usage:")
        console.print("    aoc help       - Displays this help text")
        console.print("    aoc init [day] - Creates a new directory structure for the given day, or today, if no day is supplied.")
        console.print("    aoc run <day>  - Runs the code for the given day with the main input")
        console.print("    aoc test <day> - Runs the code for the given day with testing input")
    elif sys.argv[1] == "init":
        # Initializing a new day
        day = getDay()
        with console.status(f"Initializing day {day}..."):
            makeNewDay(day, console)
            getInput(day, console)

    elif sys.argv[1] == "run":
        day = getDay()
        with console.status(f"Running day {day}..."):
            runDay(day, console)
            
    elif sys.argv[1] == "test":
        day = getDay()
        with console.status(f"Testing day {day}..."):
            testDay(day, console)