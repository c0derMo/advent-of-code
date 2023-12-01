import re
from math import floor

REGEX_MONKEY = r"Monkey \d+:"
REGEX_STARTING_ITEMS = r"  Starting items: (\d+(?:, \d+)*)?"
REGEX_OPERATION = r"  Operation: new = (old|\d+) (\*|\+) (old|\d+)"
REGEX_TEST = r"  Test: divisible by (\d+)"
REGEX_TEST_IF_TRUE = r"    If true: throw to monkey (\d+)"
REGEX_TEST_IF_FALSE = r"    If false: throw to monkey (\d+)"

def task1(inputLines):
    monkeys = buildMonkeys(inputLines)
    
    # print(monkeys)

    for i in range(20):
        print(f"R{i}")
        for monkey in monkeys:
            print("new M")
            for item in monkey["items"]:
                # print(f"Looking at item {item}")
                op1 = 0
                op2 = 0
                if monkey["operation"]["operand1"] == "old":
                    op1 = int(item)
                else:
                    op1 = int(monkey["operation"]["operand1"])
                if monkey["operation"]["operand2"] == "old":
                    op2 = int(item)
                else:
                    op2 = int(monkey["operation"]["operand2"])
                if monkey["operation"]["operation"] == "+":
                    new = op1 + op2
                elif monkey["operation"]["operation"] == "*":
                    new = op1 * op2
                else:
                    raise ValueError(f"Unknown operation {monkey['operation']['operation']}")
                # print(f"New value is {new} ({op1} {monkey['operation']['operation']} {op2})")
                
                new = floor(new / 3.0)

                if new % monkey['test'] == 0:
                    # Throw true
                    # print(f"Is divisible by {monkey['test']}, throwing to {int(monkey['trueThrow'])}")
                    monkeys[int(monkey['trueThrow'])]['items'].append(new)
                else:
                    # print(f"Is not divisible by {monkey['test']}, throwing to {int(monkey['falseThrow'])}")
                    monkeys[int(monkey['falseThrow'])]['items'].append(new)
                # return
                monkey['inspected'] += 1
            monkey['items'] = []
    
    # Find two highest inspectors
    max1 = 0
    max2 = 0
    for monkey in monkeys:
        if monkey['inspected'] > max1:
            max2 = max1
            max1 = monkey['inspected']
        elif monkey['inspected'] > max2:
            max2 = monkey['inspected']
    
    # print(monkeys)
    print(max1 * max2)


def task2(inputLines):
    monkeys = buildMonkeys(inputLines)
    mod = 0
    for monkey in monkeys:
        mod += int(monkey['test'])
    
    # print(monkeys)

    for i in range(10000):
        if i % 100 == 0:
            print(f"R{i}")
        for monkey in monkeys:
            # print("new M")
            for item in monkey["items"]:
                # print(f"Looking at item {item}")
                op1 = 0
                op2 = 0
                if monkey["operation"]["operand1"] == "old":
                    op1 = int(item)
                else:
                    op1 = int(monkey["operation"]["operand1"])
                if monkey["operation"]["operand2"] == "old":
                    op2 = int(item)
                else:
                    op2 = int(monkey["operation"]["operand2"])
                if monkey["operation"]["operation"] == "+":
                    new = op1 + op2
                elif monkey["operation"]["operation"] == "*":
                    new = op1 * op2
                else:
                    raise ValueError(f"Unknown operation {monkey['operation']['operation']}")
                # print(f"New value is {new} ({op1} {monkey['operation']['operation']} {op2})")

                new = new % mod

                if new % monkey['test'] == 0:
                    # Throw true
                    # print(f"Is divisible by {monkey['test']}, throwing to {int(monkey['trueThrow'])}")
                    monkeys[int(monkey['trueThrow'])]['items'].append(new)
                else:
                    # print(f"Is not divisible by {monkey['test']}, throwing to {int(monkey['falseThrow'])}")
                    monkeys[int(monkey['falseThrow'])]['items'].append(new)
                # return
                monkey['inspected'] += 1
            monkey['items'] = []
    
    # Find two highest inspectors
    max1 = 0
    max2 = 0
    for monkey in monkeys:
        print(monkey['inspected'])
        if monkey['inspected'] > max1:
            max2 = max1
            max1 = monkey['inspected']
        elif monkey['inspected'] > max2:
            max2 = monkey['inspected']
    
    # print(monkeys)
    print(max1 * max2)

def buildMonkeys(inputLines: [str]) -> [dict]:
    monkeys = []
    for line in inputLines:
        if re.match(REGEX_MONKEY, line):
            monkeys.append({
                "items": [],
                "operation": {
                    "operand1": "",
                    "operand2": "",
                    "operation": ""
                },
                "test": 0,
                "trueThrow": 0,
                "falseThrow": 0,
                "inspected": 0
            })
        elif re.match(REGEX_STARTING_ITEMS, line):
            match = re.match(REGEX_STARTING_ITEMS, line)
            monkeys[len(monkeys)-1]["items"] = match.group(1).split(", ")
        elif re.match(REGEX_OPERATION, line):
            match = re.match(REGEX_OPERATION, line)
            monkeys[len(monkeys)-1]["operation"]["operand1"] = match.group(1)
            monkeys[len(monkeys)-1]["operation"]["operation"] = match.group(2)
            monkeys[len(monkeys)-1]["operation"]["operand2"] = match.group(3)
        elif re.match(REGEX_TEST, line):
            match = re.match(REGEX_TEST, line)
            monkeys[len(monkeys)-1]["test"] = int(match.group(1))
        elif re.match(REGEX_TEST_IF_FALSE, line):
            match = re.match(REGEX_TEST_IF_FALSE, line)
            monkeys[len(monkeys)-1]["falseThrow"] = int(match.group(1))
        elif re.match(REGEX_TEST_IF_TRUE, line):
            match = re.match(REGEX_TEST_IF_TRUE, line)
            monkeys[len(monkeys)-1]["trueThrow"] = int(match.group(1))
    return monkeys