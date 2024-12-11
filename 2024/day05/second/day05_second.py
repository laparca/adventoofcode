#!/usr/bin/env python3
from functools import cmp_to_key

f = open("input.txt")
data = f.read().split("\n")
#data = [
#"47|53",
#"97|13",
#"97|61",
#"97|47",
#"75|29",
#"61|13",
#"75|53",
#"29|13",
#"97|29",
#"53|29",
#"61|53",
#"97|53",
#"61|29",
#"47|13",
#"75|47",
#"97|75",
#"47|61",
#"75|61",
#"47|29",
#"75|13",
#"53|13",
#"",
##"75,47,61,53,29",
##"97,61,53,29,13",
##"75,29,13",
##"75,97,47,61,53",
##"61,13,29",
#"97,13,75,29,47"
#"75,97,47,61,53",
##"97,13,75,29,47"
#]

def parse_data(d):
    from_to = {}
    to_from = {}
    all_nodes = []

    entries = []
    for l in d:
        s = l.split('|')
        if len(s) == 2:
            if not s[0] in from_to:
                from_to[s[0]] = []
            from_to[s[0]].append(s[1])

            if not s[0] in all_nodes:
                all_nodes.append(s[0])
            if not s[1] in all_nodes:
                all_nodes.append(s[1])

        elif len(l) > 0:
            entries.append(l.split(','))
    
    return from_to, all_nodes, entries

def is_good_entry(from_to, entry):
    for i in range(len(entry)-1):
        for j in range(i+1, len(entry)):
            if not entry[j] in from_to:
                continue
            if entry[i] in from_to[entry[j]]:
                return False
    return True

def is_less_than(whole, a, b):
    if not a in whole:
        return False
    if b in from_to[a]:
        return True
    return False


def fix_order(whole, entry):
    if len(entry) <= 1:
        return entry

    if len(entry) == 2:
        return entry if is_less_than(whole, entry[0], entry[1]) else [entry[1], entry[0]]

    pivot = int(len(entry)/2)

    left  = [x for x in entry if     is_less_than(whole, x, entry[pivot])]
    right = [x for x in entry if x != entry[pivot] and not is_less_than(whole, x, entry[pivot])]

    return fix_order(whole, left) + [entry[pivot]] + fix_order(whole, right)

def calculate_whole(from_to, reference, whole):
    if not reference in from_to: return
    if reference in whole: return

    whole[reference] = from_to[reference]
    for to in from_to[reference]:
        calculate_whole(from_to, to, whole)
        if to in whole:
            whole[reference] = list(set(whole[reference]) | set(whole[to]))


def whole_relations(from_to, all_nodes):
    whole = {}
    for f in from_to:
        calculate_whole(from_to, f, whole)
    return whole

def custom_cmp(whole):
    def func(a, b):
        return is_less_than(whole, a, b)
    return func

from_to, all_nodes, entries = parse_data(data)
print("loaded. There are ", len(entries), " entries")
whole = whole_relations(from_to, all_nodes)
accum = 0
for entry in entries:
    if not is_good_entry(from_to, to_from, entry):
        entry = fix_order(whole, entry)
        accum += int(entry[int(len(entry) / 2)])
print(accum)
