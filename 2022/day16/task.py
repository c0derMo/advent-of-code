import re
import collections
import itertools

REGEX_VALVE = r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z]{2}(, [A-Z]{2})*)"

def task1(inputLines):
    valves = buildValves(inputLines)
    # print(valves)

    optimizedGraph = optimizeGraph(valves)
    # print(optimizedGraph)

    flow = optimizeFlow(optimizedGraph, 30)
    print(f"Max achievable flow: {flow}")

def task2(inputLines):
    valves = buildValves(inputLines)
    # print(valves)

    optimizedGraph = optimizeGraph(valves)
    # print(optimizedGraph)

    flow = optimize2Flow(optimizedGraph)
    print(f"Max achievable flow: {flow}")

def buildValves(lines):
    valves = {}
    for line in lines:
        match = re.match(REGEX_VALVE, line)
        if not match:
            raise ValueError(f"Line '{line}' doesnt match regex")
        valveName = match.group(1)
        valveFlow = int(match.group(2))
        valveConnections = match.group(3).split(", ")
        valves[valveName] = {
            'flow': valveFlow,
            'connections': valveConnections
        }
    return valves

def bfs(allValves, start):
    queue = collections.deque([(0, start)])
    paths = {}
    while queue:
        distance, node = queue.popleft()
        if node in paths:
            continue
        paths[node] = distance
        for neighbor in allValves[node]['connections']:
            queue.append((distance + 1, neighbor))
    return paths

def optimizeGraph(valves):
    optimized = {}
    for valve in valves:
        if valves[valve]['flow'] == 0 and valve != "AA":
            continue
        paths = bfs(valves, valve)
        paths.pop(valve)
        optimized[valve] = {
            'flow': valves[valve]['flow'],
            'connections': {}
        }
        for path in paths:
            if valves[path]['flow'] == 0:
                continue
            optimized[valve]['connections'][path] = paths[path]
    return optimized

def optimizeFlow(graph, minutes):
    maxMinutes = minutes
    maxFlow = 0

    queue = collections.deque([(0, 0, "AA", set(graph) - {"AA"})])
    while queue:
        minutesPassed, currentFlow, currentPosition, closedValves = queue.popleft()

        for closedValve in closedValves:
            distanceToValve = graph[currentPosition]['connections'][closedValve]
            # Check if path is too long
            if distanceToValve >= maxMinutes - minutesPassed:
                continue

            newFlow = currentFlow + (graph[closedValve]['flow']) * (maxMinutes - minutesPassed - distanceToValve - 1)
            queue.append((minutesPassed + 1 + distanceToValve, newFlow, closedValve, closedValves - {closedValve}))
            if newFlow > maxFlow:
                maxFlow = newFlow
    return maxFlow

def optimize2Flow(graph):
    # Split the valves in two groups
    rooms = set(graph) - {"AA"}
    amountRoomsPerPerson = len(rooms) // 2

    combinations = []

    for combination in itertools.combinations(sorted(rooms), amountRoomsPerPerson):
        combinations.append((set(combination), rooms - set(combination)))
    
    maxFlow = 0

    for combination in combinations:
        group1 = combination[0]
        group2 = combination[1]
        group1.add("AA")
        group2.add("AA")
        graph1 = {}
        graph2 = {}
        for valve in graph:
            if valve in group1:
                graph1[valve] = {
                    'flow': graph[valve]['flow'],
                    'connections': {}
                }
                for v2 in graph[valve]['connections']:
                    if v2 in group1:
                        graph1[valve]['connections'][v2] = graph[valve]['connections'][v2]
            if valve in group2:
                graph2[valve] = {
                    'flow': graph[valve]['flow'],
                    'connections': {}
                }
                for v2 in graph[valve]['connections']:
                    if v2 in group2:
                        graph2[valve]['connections'][v2] = graph[valve]['connections'][v2]
            if not valve in group1 and not valve in group2:
                raise ValueError(f"Valve {valve} is in no group")
        flow = optimizeFlow(graph1, 26) + optimizeFlow(graph2, 26)
        if flow > maxFlow:
            maxFlow = flow
    
    return maxFlow


    maxMinutes = 26
    maxFlow = 0
    queue = collections.deque([
        (0, "AA", "AA", 0, 0, set(graph) - {"AA"})
    ])
    while queue:
        currentFlow, currentPos1, currentPos2, busyUntil1, busyUntil2, closedValves = queue.popleft()

        # Doing calculations for p1
        for closedValve1 in closedValves:
            distanceToValve1 = graph[currentPos1]['connections'][closedValve1]
            # Check if path is too long
            p1Move = True
            if distanceToValve1 >= maxMinutes - busyUntil1:
                # p1Move = False
                continue

            # P1 moves to closedValve1

            # Doing calculations for p2
            for closedValve2 in closedValves:
                # We dont move to the same one
                p2Move = True
                if closedValve2 == closedValve1 and p1Move:
                    # p2Move = False
                    continue
                distanceToValve2 = graph[currentPos2]['connections'][closedValve2]
                # Check if path is too long
                if distanceToValve2 >= maxMinutes - busyUntil2:
                    # p2Move = False
                    continue
                
                if not p1Move and not p2Move:
                    continue

                newFlow = currentFlow
                newPos1 = currentPos1
                newPos2 = currentPos2
                newBusyUntil1 = busyUntil1
                newBusyUntil2 = busyUntil2
                newClosedValves = closedValves.copy()
                if p1Move:
                    newPos1 = closedValve1
                    newFlow += (graph[closedValve1]['flow']) * (maxMinutes - busyUntil1 - distanceToValve1 - 1)
                    newBusyUntil1 += 1 + distanceToValve1
                    newClosedValves -= {closedValve1}
                if p2Move:
                    newPos2 = closedValve2
                    newFlow += (graph[closedValve2]['flow']) * (maxMinutes - busyUntil2 - distanceToValve2 - 1)
                    newBusyUntil2 += 1 + distanceToValve2
                    newClosedValves -= {closedValve2}
                queue.append((newFlow, newPos1, newPos2, newBusyUntil1, newBusyUntil2, newClosedValves))
                if newFlow > maxFlow:
                    maxFlow = newFlow
    return maxFlow