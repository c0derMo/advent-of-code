def task1(input_lines: list[str]):
    correct_triangles = 0

    for triangle in input_lines:
        numbers = [int(x) for x in triangle.split()]
        if is_valid_triangle(numbers[0], numbers[1], numbers[2]):
            correct_triangles += 1
    
    print(correct_triangles)

def task2(input_lines: list[str]):
    correct_triangles = 0

    for i in range(0, len(input_lines), 3):
        n1 = [int(x) for x in input_lines[i].split()]
        n2 = [int(x) for x in input_lines[i+1].split()]
        n3 = [int(x) for x in input_lines[i+2].split()]

        # t1
        if is_valid_triangle(n1[0], n2[0], n3[0]):
            correct_triangles += 1
        # t2
        if is_valid_triangle(n1[1], n2[1], n3[1]):
            correct_triangles += 1
        # t3
        if is_valid_triangle(n1[2], n2[2], n3[2]):
            correct_triangles += 1
    
    print(correct_triangles)


def is_valid_triangle(a: int, b: int, c: int) -> bool:
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if a + c <= b:
        return False
    return True