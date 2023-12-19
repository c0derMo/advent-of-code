import re

def task1(input_lines: list[str]):
    workflow_lines = []
    part_lines = []
    part = False
    for line in input_lines:
        if line == "":
            part = True
        elif part:
            part_lines.append(line)
        else:
            workflow_lines.append(line)
    workflows = parse_workflows(workflow_lines)
    print(workflows)

    result = 0
    for part_raw in part_lines:
        part = parse_part(part_raw)
        if is_part_accepted(part, workflows):
            result += part[0] + part[1] + part[2] + part[3]
    print(result)

def task2(input_lines: list[str]):
    workflow_lines = []
    part_lines = []
    part = False
    for line in input_lines:
        if line == "":
            part = True
        elif part:
            part_lines.append(line)
        else:
            workflow_lines.append(line)
    workflows = parse_workflows(workflow_lines)
    print(workflows)

    possibilities = get_possibilities_for_accepting(workflows)
    print(possibilities)

REGEX_WORKFLOW = re.compile(r"(\w+)\{(.+)\}")
REGEX_PART = re.compile(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}")

def parse_workflows(workflows: list[str]) -> dict[str, list[tuple[int, str, int, str]]]:
    parsed_workflows = {}
    for line in workflows:
        match = REGEX_WORKFLOW.match(line)
        if match is None:
            raise ValueError(f"Workflow {line} doesnt match pattern :(")
        steps = []
        steps_raw = match.group(2).split(",")
        for step in steps_raw:
            if "<" in step or ">" in step:
                match step[0]:
                    case "x":
                        attribute = 0
                    case "m":
                        attribute = 1
                    case "a":
                        attribute = 2
                    case "s":
                        attribute = 3
                operator = step[1]
                compare_to = int(step[2:].split(":")[0])
                result = step[2:].split(":")[1]
                steps.append((attribute, operator, compare_to, result))
            else:
                steps.append((-1, "", -1, step))
        parsed_workflows[match.group(1)] = steps
    return parsed_workflows

def parse_part(line: str) -> tuple[int, int, int, int]:
    match = REGEX_PART.match(line)
    if match is None:
        raise ValueError(f"Part {line} doesnt match pattern :(")
    return int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))

def is_part_accepted(part: tuple[int, int, int, int], workflows: dict[str, list[tuple[int, str, int, str]]], current_workflow="in") -> bool:
    for step in workflows[current_workflow]:
        attribute, operator, compare_to, result = step
        step_accepted = False
        if attribute < 0:
            step_accepted = True
        else:
            if operator == ">":
                if part[attribute] > compare_to:
                    step_accepted = True
            elif operator == "<":
                if part[attribute] < compare_to:
                    step_accepted = True
            else:
                raise ValueError(f"Invalid operator: {operator}")


        if step_accepted:
            if result == "A":
                return True
            if result == "R":
                return False
            return is_part_accepted(part, workflows, result)
    raise ValueError("Workflow ended without result")

def get_possibilities_for_accepting(workflows: dict[str, list[tuple[int, str, int, str]]]) -> int:
    possibilities = 0
    all_accepting_ranges = get_ranges_for_accepting(workflows)

    for i, accepting_range in enumerate(all_accepting_ranges):
        local_possibilities = accepting_range[0][1] - accepting_range[0][0] + 1
        if local_possibilities <= 0:
            # Impossible to reach this result
            continue
        local_possibilities *= accepting_range[1][1] - accepting_range[1][0] + 1
        if local_possibilities <= 0:
            # Impossible to reach this result
            continue
        local_possibilities *= accepting_range[2][1] - accepting_range[2][0] + 1
        if local_possibilities <= 0:
            # Impossible to reach this result
            continue
        local_possibilities *= accepting_range[3][1] - accepting_range[3][0] + 1
        if local_possibilities <= 0:
            # Impossible to reach this result
            continue
        possibilities += local_possibilities

    return possibilities


def get_ranges_for_accepting(workflows: dict[str, list[tuple[int, str, int, str]]], target="A", bounds=[(1,4000),(1,4000),(1,4000),(1,4000)]) -> list[tuple[tuple[int, int],tuple[int, int],tuple[int, int],tuple[int, int]]]:
    accepting_ranges = []

    for workflow, steps in workflows.items():
        local_bounds = [b for b in bounds]

        for step in steps:

            if step[3] == target:
                # print(f"Found workflow with target {workflow}")
                # This workflow has an accepting state, we need to figure out how to get to it
                hitting_bounds = [b for b in local_bounds]
                if step[0] >= 0:
                    lower, upper = hitting_bounds[step[0]]
                    if step[1] == "<":
                        upper = min(step[2] - 1, upper)
                    if step[1] == ">":
                        lower = max(step[2] + 1, lower)
                    hitting_bounds[step[0]] = (lower, upper)
                    
                if workflow == "in":
                    # print(hitting_bounds)
                    accepting_ranges.append(hitting_bounds)
                else:
                    accepting_ranges.extend(get_ranges_for_accepting(workflows, workflow, hitting_bounds))
            
    
            if step[0] >= 0:
                lower, upper = local_bounds[step[0]]
                if step[1] == "<":
                    lower = max(step[2], lower)
                if step[1] == ">":
                    upper = min(step[2], upper)
                local_bounds[step[0]] = (lower, upper)
    return accepting_ranges