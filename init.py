import sys
import os
import shutil
import requests
from datetime import date
from rich.progress import Progress
from rich import print

AOC_BASE_URL = "https://adventofcode.com"
AOC_YEAR = 2022

def makeNewDay(day, progress, task):
    newDirectoryPath = f"src/day{str(day).rjust(2, '0')}"

    # Create new directory
    if not os.path.exists(newDirectoryPath):
        os.mkdir(newDirectoryPath)
    progress.update(task, advance=1)

    # Copy files - just python for now
    shutil.copytree(".aoc/file_templates/python/", newDirectoryPath + "/", dirs_exist_ok=True)
    progress.update(task, advance=1)

def getInput(day, progress, task):
    if not os.path.exists(".aoc/SESSION_TOKEN"):
        print("You need to write your session token to the file '.aoc/SESSION_TOKEN' in order to download your input!")
        progress.update(task, advance=2)
        return
    tokenFile = open(".aoc/SESSION_TOKEN")
    AOC_SESSION_COOKIE = tokenFile.read()
    tokenFile.close()

    response = requests.get(url=f"{AOC_BASE_URL}/{AOC_YEAR}/day/{str(day)}/input", cookies={"session": AOC_SESSION_COOKIE})
    if response.ok:
        progress.update(task, advance=1)
        data = response.text
        file = open(f"src/day{str(day).rjust(2, '0')}/input", "w+")
        file.write(data.rstrip("\n"))
        file.close()
    else:
        print("Error while getting input")
    progress.update(task, advance=1)

if __name__ == '__main__':
    with Progress() as progress:
        task = progress.add_task("Creating new day structure...", total=4)

        day = -1
        if len(sys.argv) >= 2:
            try:
                day = int(sys.argv[1])
            except:
                pass
        else:
            day = date.today().day
        if day <= 0 or day >= 25:
            print("Invalid day. Should be 1-25, was " + str(day))
            exit(1)
        
        makeNewDay(day, progress, task)
        getInput(day, progress, task)