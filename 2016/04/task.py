from dataclasses import dataclass
import re

def task1(input_lines: list[str]):
    rooms = parse_rooms(input_lines)

    sum_of_sector_ids = 0

    for room in rooms:
        if is_real(room):
            sum_of_sector_ids += room.sector_id
    
    print(sum_of_sector_ids)

def task2(input_lines: list[str]):
    rooms = parse_rooms(input_lines)

    for room in rooms:
        decoded_parts = []
        # print(room.name)
        for part in room.name:
            new_part = ""
            for char in part:
                new_part += rotate_forward(char, room.sector_id)
            decoded_parts.append(new_part)
            # print(decoded_parts)
        decoded_name = " ".join(decoded_parts)
        print(decoded_name)
        if "north" in decoded_name:
            print("Hooray:")
            print(room.sector_id)
            return
    
    print("No result :/")


@dataclass
class Room:
    name: list[str]
    sector_id: int
    checksum: str

def parse_rooms(rooms: list[str]) -> list[Room]:
    result = []

    regex = re.compile(r"([\w-]+)-(\d+)\[(\w+)\]")

    for line in rooms:
        matcher = regex.match(line)
        if matcher is None:
            raise ValueError(f"Invalid room: {line}")

        name = matcher.group(1).split("-")
        sector_id = int(matcher.group(2))
        checksum = matcher.group(3)

        result.append(
            Room(name, sector_id, checksum)
        )
    
    return result

def is_real(room: Room) -> bool:
    char_amounts = {}

    # adding defaults
    for x in "abcdefghijklmnopqrstuvwxyz":
        char_amounts[x] = 0
    
    for part in room.name:
        for char in part:
            char_amounts[char] += 1
    
    all_chars = [x for x in "abcdefghijklmnopqrstuvwxyz"]
    all_chars.sort(key=lambda x: char_amounts[x], reverse=True)

    return room.checksum == "".join(all_chars[:5])

def rotate_forward(s: str, rotate_by: int) -> str:
    old = ord(s) - 97
    old += rotate_by
    old %= 26
    # print(old)
    return chr(old + 97)