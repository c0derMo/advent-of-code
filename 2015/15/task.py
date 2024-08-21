from dataclasses import dataclass
import re


def task1(input_lines: list[str]):
    ingredients = [parse_ingredient(x) for x in input_lines]

    possible_amounts = generate_amounts(len(ingredients))

    scores = [get_cookie_score(ingredients, x) for x in possible_amounts]

    print(max(scores))

def task2(input_lines: list[str]):
    ingredients = [parse_ingredient(x) for x in input_lines]

    possible_amounts = generate_amounts(len(ingredients))

    scores = [get_cookie_score_with_calories(ingredients, x) for x in possible_amounts]
    actual_scores = [x[0] for x in scores if x[1] <= 500]

    print(max(actual_scores))

@dataclass(init=True)
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

def parse_ingredient(ingredient: str) -> Ingredient:
    pattern = re.compile(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")
    matcher = pattern.match(ingredient)
    if matcher is None:
        raise ValueError(f"Ingredient {ingredient} does not match regex")
    ing = Ingredient(matcher.group(1), int(matcher.group(2)), int(matcher.group(3)), int(matcher.group(4)), int(matcher.group(5)), int(matcher.group(6)))
    return ing

def generate_amounts(num_variables: int, max_val=100) -> list[list[int]]:
    result = []
    for i in range(1, max_val+1):
        if num_variables == 1:
            result.append([i])
        else:
            sub_solutions = generate_amounts(num_variables-1, max_val-i)
            for sub_solution in sub_solutions:
                r = [i]
                r.extend(sub_solution)
                result.append(r)
    return result

def get_cookie_score(ingredients: list[Ingredient], amounts: list[int]) -> int:
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for i in range(len(ingredients)):
        capacity += ingredients[i].capacity * amounts[i]
        durability += ingredients[i].durability * amounts[i]
        flavor += ingredients[i].flavor * amounts[i]
        texture += ingredients[i].texture * amounts[i]
    
    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0
    
    return capacity * durability * flavor * texture

def get_cookie_score_with_calories(ingredients: list[Ingredient], amounts: list[int]) -> tuple[int, int]:
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    for i in range(len(ingredients)):
        capacity += ingredients[i].capacity * amounts[i]
        durability += ingredients[i].durability * amounts[i]
        flavor += ingredients[i].flavor * amounts[i]
        texture += ingredients[i].texture * amounts[i]
        calories += ingredients[i].calories * amounts[i]
    
    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0
    
    return tuple([capacity * durability * flavor * texture, calories])