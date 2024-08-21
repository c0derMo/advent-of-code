import math
def task1(input_lines: list[str]):
    target_num = int(input_lines[0]) / 10
    house_num = math.floor(math.sqrt(target_num))
    while True:
        presents = presents_at_house(house_num)
        if presents >= target_num:
            print(house_num)
            return
        house_num += 1

def task2(input_lines: list[str]):
    target_num = int(input_lines[0]) / 11
    house_num = 720720
    print(presents_at_house(51))
    print(presents_at_house_with_exhaustion(51))
    while True:
        presents = presents_at_house_with_exhaustion(house_num)
        if presents >= target_num:
            print(house_num)
            return
        house_num += 1

def presents_at_house(housenum: int):
    house_gifts = 0
    for elfnum in range(1, int(math.sqrt(housenum)) + 1):
        if housenum % elfnum == 0:
            house_gifts += elfnum
            print(f"Elf {elfnum} delivers to house {housenum}")
            if elfnum != housenum // elfnum:
                house_gifts += housenum // elfnum
                print(f"Elf {housenum // elfnum} delivers to house {housenum}")
    return house_gifts

def presents_at_house_with_exhaustion(housenum: int):
    house_gifts = 0
    for elfnum in range(1, int(math.sqrt(housenum)) + 1):
        if housenum % elfnum == 0:
            if (housenum // elfnum) <= 50:
                house_gifts += elfnum
                # print(f"Elf {elfnum} delivers to house {housenum}")
            if elfnum != housenum // elfnum:
                if housenum // (housenum // elfnum) <= 50:
                    house_gifts += housenum // elfnum
                    # print(f"Elf {housenum // elfnum} delivers to house {housenum}")
    return house_gifts