from dataclasses import dataclass

MAX_SIZE = 100000

@dataclass
class Directory():
    directSize: int
    name: str
    containsDirectories: []

    def addFile(self, size):
        self.directSize += size
    
    def addDirectory(self, subDirectory):
        self.containsDirectories.append(subDirectory)
    
    def totalSize(self):
        s = self.directSize
        for d in self.containsDirectories:
            s += d.totalSize()
        return s

def task1(inputLines):
    (tree, directories) = buildDirectoryTree(inputLines)
    result = 0
    for d in directories:
        if d.totalSize() <= MAX_SIZE:
            result += d.totalSize()
    print(result)

def task2(inputLines):
    (tree, directories) = buildDirectoryTree(inputLines)
    freeSpace = 70000000 - tree["/"].totalSize()
    missingSpace = 30000000 - freeSpace
    
    minPossibility = 70000000

    for d in directories:
        if d.totalSize() >= missingSpace:
            minPossibility = min(minPossibility, d.totalSize())
    
    print(minPossibility)

def buildDirectoryTree(lines: [str]):
    tree = {}
    directories = []
    cwd = []
    for line in lines:
        cols = line.split(" ")
        if cols[0] == "$":
            # We got a command
            if cols[1] == "cd":
                if cols[2] == "/":
                    cwd = []
                elif cols[2] == "..":
                    cwd.pop()
                else:
                    newPath = listToPath(cwd, cols[2])
                    if newPath not in tree.keys():
                        d2 = Directory(0, newPath, [])
                        directories.append(d2)
                        tree[listToPath(cwd)].addDirectory(d2)
                        tree[newPath] = d2
                    cwd.append(cols[2])
                if listToPath(cwd) not in tree.keys():
                    d = Directory(0, listToPath(cwd), [])
                    directories.append(d)
                    tree[listToPath(cwd)] = d
            elif cols[1] == "ls":
                pass
            else:
                raise ValueError(f"Unknown command {cols[1]}")
        else:
            # We're ls-ing
            if listToPath(cwd) not in tree.keys():
                d = Directory(0, listToPath(cwd), [])
                directories.append(d)
                tree[listToPath(cwd)] = d
            if cols[0] == "dir":
                subDirPath = listToPath(cwd, cols[1])
                if subDirPath not in tree.keys():
                    d2 = Directory(0, subDirPath, [])
                    directories.append(d2)
                    tree[listToPath(cwd)].addDirectory(d2)
                    tree[subDirPath] = d2
                pass
            else:
                tree[listToPath(cwd)].addFile(int(cols[0]))
    return (tree, directories)

def listToPath(cwd, nextDirectory=""):
    if nextDirectory != "":
        c = cwd.copy()
        c.append(nextDirectory)
        return "/" + "/".join(c)
    else:
        return "/" + "/".join(cwd)