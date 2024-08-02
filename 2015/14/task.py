import math
import re


def task1(input_lines: list[str]):
    reindeers = [parse_reindeer(x) for x in input_lines]

    for reindeer in reindeers:
        reindeer.simulate_seconds(2503)
    
    distances = [x.current_distance for x in reindeers]
    print(max(distances))

def task2(input_lines: list[str]):
    reindeers = [parse_reindeer(x) for x in input_lines]
    scores = [0 for _ in reindeers]

    for _ in range(2503):
        for reindeer in reindeers:
            reindeer.simulate_seconds(1)
        winner = -1
        winning_distance = 0
        for idx, reindeer in enumerate(reindeers):
            if reindeer.current_distance > winning_distance:
                winner = idx
                winning_distance = reindeer.current_distance
        scores[winner] += 1
    
    winner = -1
    winning_distance = 0
    for idx, reindeer in enumerate(reindeers):
        if reindeer.current_distance > winning_distance:
            winner = idx
            winning_distance = reindeer.current_distance
    scores[winner] += 1
    
    print(max(scores))

class Reindeer:
    speed: int
    time_flying: int
    time_resting: int
    name: str

    current_distance: int
    current_time: int
    is_resting: bool

    def __init__(self, name: str, speed: int, time_flying: int, time_resting: int) -> None:
        self.name = name
        self.speed = speed
        self.time_flying = time_flying
        self.time_resting = time_resting

        self.current_distance = 0
        self.current_time = 0
        self.is_resting = False
    
    def simulate_seconds(self, seconds: int) -> None:
        if seconds > self.time_flying + self.time_resting:
            cycles = math.floor(seconds / (self.time_flying + self.time_resting))
            self.current_distance += cycles * self.speed * self.time_flying
            remaining_seconds = seconds - (cycles * (self.time_flying + self.time_resting))
            if remaining_seconds > 0:
                self.simulate_seconds(remaining_seconds)
        elif self.is_resting:
            required_seconds_to_complete_cycle = self.time_resting - self.current_time
            seconds_spent = min(required_seconds_to_complete_cycle, seconds)
            remaining_seconds = seconds - seconds_spent
            self.current_time += seconds_spent
            if self.current_time >= self.time_resting:
                self.current_time = 0
                self.is_resting = False
            if remaining_seconds > 0:
                self.simulate_seconds(remaining_seconds)
        else:
            required_seconds_to_complete_cycle = self.time_flying - self.current_time
            seconds_spent = min(required_seconds_to_complete_cycle, seconds)
            remaining_seconds = seconds - seconds_spent
            self.current_time += seconds_spent
            self.current_distance += seconds_spent * self.speed
            if self.current_time >= self.time_flying:
                self.current_time = 0
                self.is_resting = True
            if remaining_seconds > 0:
                self.simulate_seconds(remaining_seconds)


def parse_reindeer(line: str) -> Reindeer:
    pattern = re.compile("^(\\w+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds.$")
    matcher = pattern.match(line)
    if not matcher:
        raise ValueError(f"{line} does not match regex")

    return Reindeer(matcher.group(1), int(matcher.group(2)), int(matcher.group(3)), int(matcher.group(4)))