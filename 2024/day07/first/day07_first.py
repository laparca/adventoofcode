#!/usr/bin/env python3
TEST=False
if TEST:
    data =  [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20"
    ]
else:
    f = open("input.txt")
    data = f.read().split("\n")

plus = lambda a, b: a + b
mul = lambda a, b: a * b

operations = {
    '+': plus,
    '*': mul
}

def is_good_internal(expected, calculated, pending_values) -> bool:
    if len(pending_values) == 0:
        return expected == calculated
    for op in operations:
        if is_good_internal(expected, operations[op](calculated, pending_values[0]), pending_values[1:]):
            return True
    return False

def is_good(expected, values_chain) -> bool:
    return is_good_internal(expected, values_chain[0], values_chain[1:])

parsed_values = [[int(y[0]), [int(w) for w in y[1].split()]] for y in [x.split(":") for x in data]]
print(parsed_values)
print([[x[0], is_good(x[0], x[1])] for x in parsed_values])
print(sum([x[0] for x in parsed_values if is_good(x[0], x[1])]))